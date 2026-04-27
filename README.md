# Task Manager (CS50 Final Project)

## Overview

This project is a web-based Task Manager built as my final project for CS50. The main idea behind this application is to help users organize their daily tasks in a more structured way by assigning both a date and a specific time (deadline) to each task.

At the beginning, I wanted to build a simple to-do list, but I realized that most basic task apps do not handle time properly. So instead of just storing tasks, I decided to build a system that can understand deadlines and react to them. Because of this, the application is able to automatically detect when a task becomes overdue, which makes it more practical and closer to real-world usage.

The application is user-based, meaning each user must register and log in, and they only see their own tasks. This was an important design decision to make the system more realistic and secure.

---

## Features

The application supports all the essential features needed for managing tasks:

Users can register and log in securely. After logging in, they can add tasks by providing a description, a date, and a time. Tasks are stored in a database and displayed on the main page.

One feature I focused on is date filtering. Users can select a specific day and view only the tasks for that day. This makes the interface cleaner and more useful compared to showing everything at once.

Another important feature is the deadline system. Each task has a time, and the application compares it with the current time. If the time has passed and the task is not completed, it is automatically marked as overdue. This logic happens dynamically when the page loads.

Users can also mark tasks as completed or delete them. Completed tasks are visually different from pending ones, which helps users quickly understand their progress.

---

## File Structure and Explanation

The project is organized into a few main files and folders:

### app.py

This is the core of the application. It is built using Flask and contains all the routes and logic. It handles user authentication (login and registration), adding tasks, deleting tasks, marking tasks as completed, and filtering tasks by date.

It also includes the main logic for detecting overdue tasks. Instead of storing overdue status in the database, the application calculates it every time the page is loaded by comparing the task’s date and time with the current time.

---

### helpers.py

This file contains helper functions used across the application. For example, it includes the `login_required` function to restrict access to certain routes unless the user is logged in. This keeps the main code in `app.py` cleaner and more organized.

---

### templates/

This folder contains all the HTML files used for the frontend.

- `layout.html` is the base template that includes the general structure like navigation and styling.
- `index.html` is the main page where tasks are displayed, added, and managed.
- `login.html` and `register.html` handle user authentication.

These templates use Jinja to connect the backend data with the frontend display.

---

### tasks.db

This is the SQLite database used to store all the data. It includes information such as task description, date, time, status, and user ID.

---

## Technical Design

The application follows a simple structure with clear separation of responsibilities.

Flask handles the backend logic, including routing and processing user input. SQLite is used as the database because it is lightweight and easy to integrate. The frontend is built using HTML and Bootstrap to create a clean and responsive interface.

One important design decision was not to store the “overdue” status in the database. Instead, it is calculated dynamically. I chose this approach because it ensures that the status is always accurate and avoids unnecessary updates to the database.

Another decision was to keep the interface simple. Instead of adding too many features, I focused on making the existing features work correctly and reliably.

---

## How It Works

When a user logs in, the application retrieves tasks for the selected date. If no date is selected, it defaults to the current day.

Each task includes a date and time. The application combines these and compares them with the current system time. If the deadline has passed and the task is not marked as completed, it is treated as overdue and displayed differently on the page.

All user actions, such as adding or deleting tasks, are handled through Flask routes and reflected immediately in the interface.

---

## Challenges and Improvements

One of the main challenges was handling time correctly. At first, I considered storing the overdue status in the database, but I realized this could become inconsistent. Calculating it dynamically was a better solution, even though it required more careful logic.

Another challenge was organizing the structure of the project. Separating logic, templates, and helper functions helped make the code more readable and maintainable.

If I had more time, I would improve the project by adding features such as editing tasks, a calendar view, and notifications. A countdown timer showing how much time is left for each task would also make the application more interactive.

---

## Video Demo

https://youtu.be/gWzTSiR_lNM

---

## Author

Mortaza  
GitHub: mortazap53

---

## Final Thoughts

This project helped me understand how different parts of a web application work together, including backend logic, databases, and frontend design. It also gave me practical experience in solving real problems, such as handling time and managing user-specific data.

Overall, this project reflects what I learned in CS50 and how I applied it to build something functional and meaningful.
