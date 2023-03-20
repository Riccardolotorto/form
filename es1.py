#esercizio: modificare l'esercizio precedente in modo da inserire il sesso della persona che effettua il login e in caso di accesso eseguito rispondere con benvenuto o benvenuta 

from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("es1.html")

@app.route('/login', methods = ['GET'])
def login():
    nomeUtente = request.args.get('nome')
    sessoUtente = request.args.get('sesso')
    if sessoUtente == "Maschio":
        ciao = "Benvenuto"
        return render_template("login1.html", saluto = ciao, nome = nomeUtente)
    else:
        ciao = "Benvenuta"
        return render_template("login1.html", saluto = ciao, nome = nomeUtente)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)