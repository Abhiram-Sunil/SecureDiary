from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = 'securesecretkey'  # Replace with a real secret key


bcrypt = Bcrypt(app)

# CREATE DATABASE TABLE
def create_table():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diary_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
''')

    conn.commit()
    conn.close()

create_table()

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')

        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM users WHERE email = ?',
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            stored_password = user[3]

            if bcrypt.check_password_hash(stored_password, password):

              session['user'] = email

              return redirect('/dashboard')
            
        return "Invalid Email or Password"

    return render_template('login.html')

# REGISTER PAGE
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # HASH PASSWORD
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = sqlite3.connect('database.db')

        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, hashed_password)
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM diary_entries')

    entries = cursor.fetchall()

    conn.close()

    return render_template('dashboard.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():

    title = request.form['title']
    content = request.form['content']

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO diary_entries (title, content) VALUES (?, ?)',
        (title, content)
    )

    conn.commit()
    conn.close()

    return redirect('/dashboard')

@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)