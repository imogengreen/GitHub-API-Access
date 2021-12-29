from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")
if __name__ == "__app.py__":
    app.run(debug=True)

@app.route("/languages")
def languages():
    return render_template("languages.html")

@app.route("/followers")
def followers():
    return render_template("followers.html")

