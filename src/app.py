from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Lógica de autenticación aquí

    return "Inicio de sesión exitoso"


if __name__ == "__main__":
    app.run(debug=True)
