from flask import Flask, render_template

app = Flask(__name__, template_folder="app/templates")

@app.route("/")
def home():
    return render_template("dashboard/index.html")

@app.route("/about.html")
def about():
    return render_template("base.html")

@app.route("/employees.html")
def employees():
    return render_template("dashboard/index.html")

@app.route("/tasks.html")
def tasks():
    return render_template("dashboard/index.html")

if __name__ == "__main__":
    app.run(debug=True)