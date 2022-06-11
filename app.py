from flask import Flask, request, jsonify
from helpers.db_helpers import run_query

app = Flask(__name__)

@app.get('/api/animals')
def animals_get():
    # TODO: db select
    animal_list = []
    return jsonify(animal_list), 200

@app.post('/api/animals')
def animals_post():
    data = request.json
    animal_name=data.get('animalName')
    image_url=data.get('imageURL')
    # if animal_name == None
    if not animal_name:
        return jsonify("Missing required argument 'animalName'"), 422
    if not image_url:
        return jsonify("Missing required argument 'imageURL'"), 422
    # TODO: Error checking the actual values for the arguments
    # TODO: DB write