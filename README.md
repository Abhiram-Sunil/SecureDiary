# SecureDiary

SecureDiary is a cloud-based secure diary management application developed as part of a DevSecOps Capstone Project. The project demonstrates the practical implementation of cloud infrastructure, cybersecurity, Linux administration, DevOps automation, monitoring, and secure application deployment using Amazon Web Services (AWS).

## Project Overview

SecureDiary allows users to securely register, authenticate, and manage personal diary entries through a web-based interface. The application incorporates multiple security controls, automated deployment mechanisms, monitoring services, and cloud infrastructure components to provide a secure and scalable environment.

## Features

* User Registration and Login
* Role-Based Access Control (User and Admin)
* Create, Read, Update, and Delete (CRUD) Operations
* Secure Session-Based Authentication
* Password Hashing using bcrypt
* SQL Injection Prevention using Parameterized Queries
* Cross-Site Scripting (XSS) Protection
* Security Headers Implementation
* HTTPS Encryption
* Fail2Ban Brute Force Protection
* Automated Backup Storage in Amazon S3
* CloudWatch Monitoring and Logging
* Docker Containerization
* GitHub Actions CI/CD Pipeline
* Automated Deployment

## Technology Stack

### Application

* Python
* Flask
* HTML
* CSS
* JavaScript
* SQLite

### Cloud Services

* Amazon EC2
* Amazon VPC
* Amazon S3
* Amazon CloudFront
* Amazon RDS
* Application Load Balancer (ALB)
* Amazon CloudWatch

### DevOps Tools

* Git
* GitHub
* GitHub Actions
* Docker
* Nginx

### Security Controls

* HTTPS / SSL
* bcrypt Password Hashing
* Session-Based Authentication
* Security Headers
* SQL Injection Prevention
* XSS Protection
* Fail2Ban
* UFW Firewall
* AWS Security Groups

## Cloud Architecture

The SecureDiary infrastructure consists of:

* Custom AWS VPC
* Public and Private Subnets
* Internet Gateway
* Route Tables
* Application Load Balancer (ALB)
* Ubuntu EC2 Server
* Nginx Reverse Proxy
* Dockerized Flask Application
* Amazon S3 Backup Storage
* Amazon CloudWatch Monitoring
* Amazon RDS Database Service

## Monitoring and Logging

The project implements monitoring and logging using Amazon CloudWatch. Application logs and server metrics are monitored to improve visibility, operational awareness, and troubleshooting capabilities.

Monitored resources include:

* CPU Utilization
* Memory Utilization
* Application Logs
* Security Events

## Backup Strategy

Automated backup scripts generate backup files and upload them to Amazon S3. Scheduled execution is managed through Linux cron jobs to ensure regular backup operations and improved disaster recovery readiness.

## Security Features

The application follows secure development practices and incorporates multiple security mechanisms, including:

* Password Hashing
* Secure Session Management
* HTTPS Encryption
* Security Headers
* SQL Injection Prevention
* XSS Protection
* Brute Force Protection
* Firewall Controls
* Access Control Policies

## DevOps Implementation

DevOps practices implemented within the project include:

* Source Code Management using Git and GitHub
* Docker Containerization
* Continuous Integration and Continuous Deployment (CI/CD)
* Automated Deployment Workflows
* Automated Backup Operations
* Monitoring and Logging

## Project Type

DevSecOps Capstone Project

## Author

Abhiram S
