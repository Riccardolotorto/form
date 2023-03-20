from flask import Flask, render_template, request #bisogna importare la libreria request per poter fare richieste al server
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/controlla')
def controlla():
    return ("<h1>Pagina di controllo</h1>")

@app.route('/login')
def login():
    nomeUtente = request.args.get('nome')
    passwordUtente = request.args.get('password')
    if nomeUtente == "admin" and passwordUtente == "xxx123#":
        return render_template("login.html", nome = nomeUtente, password = passwordUtente)
    else:
        return render_template("errore.html", password = passwordUtente)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)