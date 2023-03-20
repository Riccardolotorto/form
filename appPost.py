from flask import Flask, render_template, request #bisogna importare la libreria request per poter fare richieste al server
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("formPost.html")

@app.route('/login', methods = ['POST'])
def login():
    nomeUtente = request.form["nome"]
    passwordUtente = request.form["password"]
    if nomeUtente == "admin" and passwordUtente == "xxx123#":
        return render_template("loginPost.html", nome = nomeUtente)
    else:
        return render_template("errore.html", password = passwordUtente)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)