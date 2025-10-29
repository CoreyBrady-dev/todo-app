from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")
        priority = request.form.get("priority")
        description = request.form.get("description")

        if title and priority and description:
            tasks.append({"title": title, "priority": priority, "description": description})
        return redirect(url_for("home"))

    return render_template("index.html", tasks=tasks)