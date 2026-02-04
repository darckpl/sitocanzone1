
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/testo")
def testo():
    return render_template("testo.html")

@app.route("/analisi")
def analisi():
    return render_template("analisi.html")

if __name__ == "__main__":
    app.run(debug=True)
