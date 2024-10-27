from flask import Flask, render_template
from api.definition_miriam import get_definition_api  # Importe une API spécifique
import os

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    apis = [
        {"name": "DÉFINITION-MIRIAM", "description": "Retrieve definitions for a given word.", "endpoint": "/definition/<word>"}
    ]
    return render_template('home.html', apis=apis)

# Enregistrement de l'API de définition
app.register_blueprint(get_definition_api, url_prefix="/definition")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
