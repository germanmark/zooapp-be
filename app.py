from flask import Flask, request, jsonify
from helpers.db_helpers import run_query
import sys

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
    return jsonify("Animal added"), 201

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print("Missing required mode argument")
    exit()
    
if mode == 'testing':
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, "0.0.0.0", 5005)
else:
    print("Mode must be in testing|production")
    exit()
    