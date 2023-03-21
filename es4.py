#Scrivere un programma per la conversione delle temperature, l'utente deve inserire un valore (float) e scegliere da una lista di radio button quale conversione effettuare, una volta selezionata una scelta, clicca su un bottone e ottiene un risultato, utilizzare le funzioni per effettuare la conversione.
from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("es4.html")


@app.route('/login', methods = ['GET'])
def login():
    valoreInserito = float(request.args.get("valoreTemperatura"))
    temperaturaFinale = request.args.get("temperaturaFinale")
    temperaturaFinale2 = request.args.get("temperaturaFinale2")
    def c_f(temperatura):
        return (temperatura * 1.8) + 32
    def f_c(temperatura):
        return (temperatura - 32) / 1.8
    def c_k(temperatura):
        return temperatura + 273.15
    if temperaturaFinale == "CF" or temperaturaFinale2 == "CF":
        ris = c_f(valoreInserito)
    elif temperaturaFinale == "FC" or temperaturaFinale2 == "FC":
        ris = f_c(valoreInserito)
    elif temperaturaFinale == "CK" or temperaturaFinale2 == "CK":
        ris = c_k(valoreInserito)
    return render_template("login4.html", risultato = ris) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)