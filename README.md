# Task Manager (CS50 Final Project)

## 📌 Overview

Task Manager is a web-based application that allows users to manage their daily tasks efficiently by assigning each task a specific date and time. The application is designed to help users stay organized, track progress, and meet deadlines.

Unlike a simple to-do list, this project introduces time-based logic, where tasks are dynamically evaluated and marked as overdue if they are not completed before their deadline.

---

## 🚀 Features

### ✅ User Authentication

* Users can register and log in securely.
* Each user has access only to their own tasks.

### 📝 Task Management

* Add tasks with:

  * Task description
  * Date
  * Time (deadline)
* Delete tasks
* Mark tasks as completed

### 📅 Date-Based Filtering

* Users can select a specific date to view tasks for that day.
* The interface updates dynamically based on the selected date.

### ⏰ Deadline & Overdue Detection

* Each task has a deadline (date + time).
* The system automatically compares the current time with the task’s deadline.
* If a task is not completed before its deadline, it is marked as:

  * **Overdue** (highlighted visually)

### 🎯 Status System

Tasks are displayed with three states:

* **Pending** – Task is not completed and still within deadline
* **Done** – Task completed by user
* **Overdue** – Deadline passed and task not completed

### 🎨 User Interface

* Built with Bootstrap for clean and responsive design
* Tasks are clearly displayed with:

  * Deadline time (“until HH:MM”)
  * Status indicators (Done / Overdue / Pending)
* Handles empty states (e.g., no tasks for selected date)

---

## 🧠 Technical Design

This project follows a simple but effective architecture:

### Backend

* Built using Flask (Python)
* Handles:

  * Routing
  * Form processing
  * Business logic (e.g., overdue detection)

### Database

* SQLite database (`tasks.db`)
* Stores:

  * Task description
  * Date
  * Time
  * Status
  * User ID

### Frontend

* HTML templates with Jinja (Flask templating)
* Bootstrap for styling

---

## ⚙️ How It Works

1. A user logs into the system.
2. The user adds a task with a date and time.
3. The task is stored in the database.
4. When the page loads:

   * The backend retrieves tasks for the selected date.
   * Python compares each task’s deadline with the current time.
   * If the deadline has passed and the task is not completed:

     * It is marked as **overdue** dynamically.
5. The frontend displays tasks with proper formatting and status.

---

## ▶️ How to Run the Project

1. Open the project in VS Code

2. Open the terminal in the project directory

3. Run the Flask application:

```bash
python -m flask run
```

4. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
task_manager/
│
├── app.py              # Main Flask application
├── tasks.db           # SQLite database
├── helpers.py         # Helper functions (login, etc.)
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── login.html
│   └── register.html
└── README.md
```

---

## 💡 Design Decisions

* **Dynamic Overdue Calculation**
  Overdue status is not stored in the database. Instead, it is calculated in real time using Python. This ensures accuracy and avoids unnecessary database updates.

* **Separation of Concerns**

  * Database → storage
  * Flask → logic
  * HTML → display

* **Simplicity & Usability**
  The interface is kept minimal and focused on functionality rather than complexity.

---

## 🔮 Future Improvements

* Calendar view (weekly/monthly)
* Task editing feature
* Countdown timer (“time remaining”)
* Notifications or reminders
* User profile and statistics

---

## 🎥 Video Demo

[https://youtu.be/FxJAEbXYJbg]

---

## 👤 Author

* Name: Mortaza
* GitHub: mortazap53

---

## 📄 License

This project was developed as part of the CS50 course.
