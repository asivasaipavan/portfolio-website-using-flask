from flask import Flask, render_template, request, redirect, url_for
import datetime
import os

app = Flask(__name__)

# Path to store contact messages
MESSAGES_FILE = "messages.txt"

def save_message(name, email, phone, message):
    ts = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    line = f"[{ts}] Name: {name} | Email: {email} | Phone: {phone} | Message: {message}\n"
    with open(MESSAGES_FILE, "a", encoding="utf-8") as f:
        f.write(line)

@app.route("/")
def home():
    # Basic profile info passed to template
    profile = {
        "name": "AMBERKAR SIVA SAI PAVAN",
        "title": "B.Tech CSE (Data Science) Student",
        "email": "238r1a67d2@gmail.com",
        "phone": "+91 7386962445",
        "summary": (
            "Enthusiastic B.Tech Computer Science Engineering (Data Science) student "
            "at CMR Engineering College with strong skills in Data Structures and "
            "Algorithms, HTML and CSS."
        )
    }
    return render_template("index.html", profile=profile)

@app.route("/projects")
def projects():
    projects_list = [
        {
            "title": "Personal Portfolio Website",
            "year": "2025",
            "desc": "Designed and developed a responsive personal portfolio using HTML, CSS and JavaScript to showcase skills and projects."
        },
        {
            "title": "To-Do List Web App",
            "year": "2025",
            "desc": "Built a task manager with add/delete/complete features and localStorage persistence."
        },
        {
            "title": "Rock–Paper–Scissors Game",
            "year": "2025",
            "desc": "Interactive browser game with player vs computer logic and score tracking."
        },
        # add more projects here if you like
    ]
    return render_template("projects.html", projects=projects_list)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            error = "Please provide at least your name, email and a message."
            return render_template("contact.html", error=error, form=request.form)

        save_message(name, email, phone, message)
        return render_template("contact.html", success=True)

    return render_template("contact.html")

if __name__ == "__main__":
    # create messages file if not exists
    if not os.path.exists(MESSAGES_FILE):
        open(MESSAGES_FILE, "w", encoding="utf-8").close()
    app.run(debug=True)
