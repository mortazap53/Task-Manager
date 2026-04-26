import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, date as dt_date

from helpers import login_required, apology

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///tasks.db")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("missing username")

        if not password:
            return apology("missing password")

        if password != confirmation:
            return apology("passwords do not match")

        hash_pw = generate_password_hash(password)

        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username,
                hash_pw
            )
        except:
            return apology("username taken")

        return redirect("/login")

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return apology("missing username")

        if not password:
            return apology("missing password")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return apology("invalid login")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ---------------- INDEX (TASKS) ----------------
from datetime import datetime

@app.route("/")
@login_required
def index():

    date = request.args.get("date")

    if not date:
        date = dt_date.today().isoformat()

    tasks = db.execute(
        "SELECT * FROM tasks WHERE user_id = ? AND date = ?",
        session["user_id"],
        date
    )

    now = datetime.now()

    for task in tasks:
        if task["status"] != "done":

            task_datetime = datetime.strptime(
                task["date"] + " " + task["time"],
                "%Y-%m-%d %H:%M"
            )

            if task_datetime < now:
                task["status"] = "overdue"

    # 🔥 THIS LINE IS CRITICAL (MUST EXIST)
    return render_template("index.html", tasks=tasks, date=date)


# ---------------- ADD TASK ----------------
@app.route("/add", methods=["POST"])
@login_required
def add():

    task = request.form.get("task")
    date = request.form.get("date")
    time = request.form.get("time")

    if not task or not date or not time:
        return apology("missing fields")

    db.execute(
        "INSERT INTO tasks (user_id, task, date, time, status) VALUES (?, ?, ?, ?, ?)",
        session["user_id"],
        task,
        date,
        time,
        "pending"
    )

    return redirect("/")


# ---------------- DONE TASK ----------------
@app.route("/done", methods=["POST"])
@login_required
def done():

    task_id = request.form.get("task_id")

    if not task_id:
        return apology("missing task")

    db.execute(
        "UPDATE tasks SET status = 'done' WHERE id = ?",
        task_id
    )

    return redirect("/")


# ---------------- DELETE TASK ----------------
@app.route("/delete/<int:task_id>")
@login_required
def delete(task_id):
    user_id = session["user_id"]

    db.execute(
        "DELETE FROM tasks WHERE id = ? AND user_id = ?",
        task_id, user_id
    )

    return redirect("/")


# ---------------- Complete Task ----------------
@app.route("/complete/<int:task_id>")
@login_required
def complete(task_id):
    user_id = session["user_id"]

    db.execute(
        "UPDATE tasks SET status = 'done' WHERE id = ? AND user_id = ?",
        task_id, user_id
    )

    return redirect("/")


