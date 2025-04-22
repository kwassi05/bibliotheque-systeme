# src/api.py
from flask import Flask, render_template
from models.livre import Livre

app = Flask(__name__, template_folder="templates", static_folder="static")

# Exemple de données
livres = [
    Livre("1234567890", "Le Petit Prince", "Antoine de Saint-Exupéry"),
    Livre("1111111111", "1984", "George Orwell")
]

@app.route("/")
def accueil():
    return render_template("index.html", livres=livres)

if __name__ == "__main__":
    app.run(debug=True)
