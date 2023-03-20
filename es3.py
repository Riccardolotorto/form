#es 3: scrivere una web app che permetta di selezionare da una lista di checkbox i propri hobby e, cliccando su un bottone avere il numero e l'elenco degli hobby selezionati
from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("es3.html")

numeroHobby = 0
@app.route('/login', methods = ['GET'])
def login():
    n1 = request.args.get("calcio")
    n2 = request.args.get("playstation")
    n3 = request.args.get("chitarra")
    global numeroHobby
    if n1 == None and n2 == None and n3 == None:
        return render_template("login3.html", nHobby = 0, hobbies = "Nulla")
    elif n1 != None:
        return render_template("login3.html", nHobby = 1, hobbies = n1)
    elif n2 != None:
        return render_template("login3.html", nHobby = 1, hobbies = n2)
    elif n3 != None:
        return render_template("login3.html", nHobby = 1, hobbies = n3) 
    
    if n1 == "Calcio" and n2 == "Playstation" and n3 == "Chitarra":
        return render_template("login3.html", nHobby = 3, hobbies = n3) 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)