from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/controlla', methods=['GET'])
def controlla():
    return ("<h1>Pagina di controllo</h1>")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)