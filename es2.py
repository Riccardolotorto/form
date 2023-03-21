#es 2: scrivere una web app che permetta di calcolare l'indice di massa corporea di una persona inserendo peso e altezza. L'app deve rispondere con una pagina contenente i valore del IMC, il responso (sottopeso, normopeso e sovrappeso) e un'immagine relativa alla dieta che deve fare
from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("es2.html")

@app.route('/login', methods = ['GET'])
def login():
    pesoUtente = int(request.args.get('peso'))
    altezzaUtente = int(request.args.get('altezza'))
    IMC = pesoUtente // ((altezzaUtente / 100) ** 2)
    if IMC < 18:
        risultato = "Sottopeso"
        foto = "static/images/mc.jpg"
        return render_template("login2.html", situazione = risultato, directory = foto)
    elif IMC >= 18 and IMC <= 24:
        foto = "static/images/pasta.jpg"
        risultato = "normopeso"
        return render_template("login2.html", situazione = risultato, directory = foto)
    elif IMC >= 25:
        risultato = "sovrappeso"
        foto = "static/images/insalata.jpg"
        return render_template("login2.html", situazione = risultato, directory = foto)
        

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)