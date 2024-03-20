from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route(
    "/",
)
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    if username == "ciao" and password == "1234":
        res = {"res": "Username e password inseriti correttamente"}
        return render_template("success.html")
    else:
        res = {"res": "Username e password errati"}
        return render_template("failed.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
