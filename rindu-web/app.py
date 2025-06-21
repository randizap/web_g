from flask import Flask, request, render_template, redirect, url_for, session
from datetime import datetime
import csv

app = Flask(__name__)
app.secret_key = "rindu_secret_key"

@app.route("/")
def home():
    return redirect("/step1")

@app.route("/step1", methods=["GET", "POST"])
def step1():
    if request.method == "POST":
        session["name"] = request.form["name"]
        return redirect("/step2")
    return render_template("step1.html")

@app.route("/step2", methods=["GET", "POST"])
def step2():
    name = session.get("name", "someone special")
    if request.method == "POST":
        return redirect("/step3")
    return render_template("step2.html", name=name)

@app.route("/step3", methods=["GET", "POST"])
def step3():
    name = session.get("name", "someone special")
    if request.method == "POST":
        answer = request.form["answer"]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open("responses.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, answer, timestamp])
        return render_template("thank_you.html", name=name, answer=answer)
    return render_template("step3.html", name=name)

if __name__ == "__main__":
    print("Open http://localhost:5000")
    app.run(debug=True, use_reloader=True)

