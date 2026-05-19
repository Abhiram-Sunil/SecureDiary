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
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
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
       "SELECT * FROM users WHERE email=?",
       (email,)
       )

        user = cursor.fetchone()

        conn.close()

        if user:

            stored_password = user[3]

            if bcrypt.check_password_hash(stored_password, password):

              session['username'] = user[1]

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

    if 'username' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(
    "SELECT * FROM entries WHERE username=?",
    (session['username'],)
    )

    entries = cursor.fetchall()

    conn.close()

    return render_template('dashboard.html', entries=entries)

@app.route('/add', methods=['GET', 'POST'])
def add():

    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':

        content = request.form['content']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO entries (username, content) VALUES (?, ?)",
            (session['username'], content)
        )

        conn.commit()
        conn.close()

        return redirect('/dashboard')

    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):

    if 'username' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM entries WHERE id=? AND username=?",
        (id, session['username'])
    )

    conn.commit()
    conn.close()

    return redirect('/dashboard')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    if 'username' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':

        content = request.form['content']

        cursor.execute(
            "UPDATE entries SET content=? WHERE id=? AND username=?",
            (content, id, session['username'])
        )

        conn.commit()
        conn.close()

        return redirect('/dashboard')

    cursor.execute(
        "SELECT * FROM entries WHERE id=? AND username=?",
        (id, session['username'])
    )

    entry = cursor.fetchone()

    conn.close()

    return render_template('edit.html', entry=entry)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)