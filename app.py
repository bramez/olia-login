from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./templates')

user = {
    'username': 'olia',
    'profile_image': 'https://mir-s3-cdn-cf.behance.net/user/230/1299a2155195935.5c4ac1e03ac9b.png',
    'personal_info': 'Me gusta leer y viajar.',
    'statistics': 'Miembros desde: 2020-06-01, Publicaciones: 100, Seguidores: 50'
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Lógica de autenticación aquí
    # hardcodear
    if username == "olia" and password == "olia88":
        print("success")
        return render_template('home.html', **user)

    else:
        print("ERROR")
        return render_template('error.html', username=username)

    # Olia homework: buscaremos en un diccionarios


if __name__ == "__main__":
    print ("Hello")
    port = 12345
    app.run(debug=True, port=port)
