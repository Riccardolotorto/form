#es 2: scrivere una web app che permetta di calcolare l'indice di massa corporea di una persona inserendo peso e altezza. L'app deve rispondere con una pagina contenente i valore del IMC, il responso (sottopeso, normopeso e sovrappeso) e un'immagine relativa alla dieta che deve fare
from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("es2.html")

@app.route('/login', methods = ['GET'])
def login():
    pesoUtente = request.args.get('peso')
    altezzaUtente = request.args.get('altezza')
    IMC = int(pesoUtente) / (int(altezzaUtente) * int(altezzaUtente))
    if IMC < 20:
        risultato = "Sottopeso"
        return render_template("login2.html", situazione = risultato)
    elif IMC >= 20 and IMC <= 30:
        risultato = "normopeso"
        return render_template("login2.html", situazione = risultato)
    elif IMC > 30:
        risultato = "sovrappeso"
        return render_template("login2.html", situazione = risultato)
        

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)