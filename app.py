from flask import Flask, render_template, request, flash, redirect, url_for
import csv 
from datetime import datetime

app = Flask(__name__)
app.secret_key="dev_secret"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        if not name or not email or not message:
            flash("All fields are required", "error")
            return redirect(url_for("contact"))
        
        with open("contacts.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message, datetime.now().isoformat()])

        flash(f"Thanks {name}, your message has been sent.", "success")
        return redirect(url_for("contact"))

    
    return render_template("contact.html")

    
