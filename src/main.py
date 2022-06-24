"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Ships
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    userList = list(map(lambda obj : obj.serialize(),users))
    print(userList)
    # cuadrados = list(map(lambda x : x ** 2, enteros))
    response_body = {
        "msg": userList
    }
    return jsonify(response_body), 200

@app.route('/character', methods=['GET'])
def get_character():
    characters = Character.query.all()
    character_list = list(map(lambda obj : obj.serialize(),characters))
    # Como character no es un objeto no se puede serializar, 
    # para eso es necesario mapearlo y extraer cada objeto del list para serializarlo
    print(character_list)
    response_body = {
        "msg": character_list
    }
    return jsonify(response_body), 200

@app.route('/planet', methods=['GET'])
def get_planet():
    planets = Planet.query.all()
    planet_list = list(map(lambda obj : obj.serialize(),planets))
    # Como character no es un objeto no se puede serializar, 
    # para eso es necesario mapearlo y extraer cada objeto del list para serializarlo
    print(planet_list)
    response_body = {
        "msg": planet_list
    }
    return jsonify(response_body), 200   

@app.route('/ship', methods=['GET'])
def get_ship():
    ships = Ships.query.all()
    ships_list = list(map(lambda obj : obj.serialize(),ships))
    # Como character no es un objeto no se puede serializar, 
    # para eso es necesario mapearlo y extraer cada objeto del list para serializarlo
    print(ships_list)
    response_body = {
        "msg": ships_list
    }
    return jsonify(response_body), 200         
        
# @app.route('/user/<int:user_id>', methods=['PUT','GET'])
# def get_single_person(user_id):
#     """
#     Single person
#     """
#     body = request.get_json() #{ 'username': 'new_username'}
#     if request.method == 'PUT':
#         user1 = User.query.get(user_id)
#         user1.user_name = body.username
#         db.session.commit()
#         return jsonify(user1.serialize()), 200
#     if request.method == 'GET':
#         user1 = User.query.get(user_id)
#         return jsonify(user1.serialize()), 200    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
