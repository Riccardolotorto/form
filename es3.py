#es 3: scrivere una web app che permetta di selezionare da una lista di checkbox i propri hobby e, cliccando su un bottone avere il numero e l'elenco degli hobby selezionati
from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("es3.html")


@app.route('/login', methods = ['GET'])
def login():
    hobbies = request.args.getlist("h")
    numeroHobby = len(hobbies)
    return render_template("login3.html", nHobby = numeroHobby, hobbies = hobbies) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)