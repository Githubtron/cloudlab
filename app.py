
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    username = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()

    return render_template("index.html", username=username)


@app.route("/health")
def health():
    return {"status": "success", "message": "Flask app is running!"}


if __name__ == "__main__":
    app.run(debug=True)