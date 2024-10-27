from flask import Blueprint, jsonify, request
import requests
import os

get_definition_api = Blueprint('get_definition_api', __name__)

@get_definition_api.route('/<word>', methods=['GET'])
def get_definition(word):
    api_key = os.getenv('API_KEY')
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and "shortdef" in data[0]:
            definitions = data[0]["shortdef"]
            return jsonify({"word": word, "definitions": definitions}), 200
        else:
            return jsonify({"error": "Definition not found"}), 404
    else:
        return jsonify({"error": "API request failed"}), 500
