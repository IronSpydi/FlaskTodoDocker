
# Flask TODO App with Docker and MySQL

> A sleek and stylish Flask TODO app that lets you organize tasks like never before!

## Introduction

The Flask Todo App is a simple web application built with Flask that allows users to manage their to-do lists. The app uses Docker and Docker Compose for easy deployment, and it utilizes a MySQL database running in a Docker container to store todo items.

## Features

- Create new tasks with ease 📝
- Update tasks effortlessly ✏️
- Mark tasks as completed ✔️
- Delete tasks when you're done 🗑️
- Responsive design for mobile and desktop 📱💻

## Prerequisites

Before you begin, make sure you have the following tools installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

To run the app locally, follow these steps:

1. Clone the repository to your machine:
   ```bash
    git clone https://github.com/your-username/fancy-flask-todo.git
    cd fancy-flask-todo

2. Create a .env file in the project's root directory to store secret credentials. Fill in the necessary values:
   ```bash
    MYSQL_ROOT_PASSWORD=your_root_password
    MYSQL_DATABASE=todo_db
    MYSQL_USER=todo_user
    MYSQL_PASSWORD=your_todo_db_password
3. Build the Docker images and start the containers:
   ```bash
    docker-compose up -d --build
4. To stop the application and clean up the containers, run the following command:
  ```bash
    docker-compose down
