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
from models import db, User, Planet, Character, Favorite
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

# INICIO PLANETS
#  Listar los registros de planets en la base de datos
@app.route('/planet', methods=['GET'])
def get_planet():

    planets = Planet.query.all()
    all_planets = list(map(lambda planet: planet.serialize(), planets))

    return jsonify(all_planets), 200

# Crear un nuevo planeta
@app.route('/planet', methods=['POST'])
def create_planet():
    body = request.get_json()
    planet = Planet(name=body["name"], diameter=body["diameter"], rotation=body["rotation"], translation=body["translation"], gravity=body["gravity"])
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize()), 201

# Modificar un planeta
@app.route('/planet/<int:planet_id>', methods=['PUT'])
def refresh_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        raise APIException("Planeta no encontrado", 404)
    body = request.get_json()
    if not ("name" in body):
        raise APIException("keyError: name", 404)
    if not ("diameter" in body):
        raise APIException("keyError: diameter", 404)
    if not ("rotation" in body):
        raise APIException("keyError: rotation", 404)
    if not ("translation" in body):
        raise APIException("keyError: translation", 404)
    if not ("gravity" in body):
        raise APIException("keyError: gravity", 404)

    planet.name = body["name"]
    planet.diameter = body["diameter"]
    planet.rotation = body["rotation"]
    planet.translation = body["translation"]
    planet.gravity = body["gravity"]

    db.session.commit()
    return jsonify(planet.serialize())

#  Listar la información de un solo planeta
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_detail_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        raise APIException("Planeta no encontrada", 404)
    return jsonify(planet.serialize())

# Borrar información de un solo planeta
@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        raise APIException("Planeta no encontradO", 404)
    db.session.delete(planet)
    db.session.commit()
    return jsonify(planet.serialize())
# FIN PLANETS

# INICIO PERSONAJES

# Listar todos los registros de prsonajes en la base de datos
@app.route('/character', methods=['GET'])
def get_characters():

    characters = Character.query.all()
    all_characters = list(map(lambda character: character.serialize(), characters))

    return jsonify(all_characters), 200

# Crear un nuevo personaje
@app.route('/character', methods=['POST'])
def create_character():

    body = request.get_json()
    character = Character(name=body["name"], eye_color=body["eye_color"], birthday_date=body["birthday_date"], gender=body["gender"], height=body["height"])
    db.session.add(character)
    db.session.commit()

    return jsonify(character.serialize()), 201

# Modificar un personaje
@app.route('/character/<int:character_id>', methods=['PUT'])
def refresh_character(character_id):
    
    character = Character.query.get(character_id)
    if character is None:
        raise APIException("Personaje no encontrado", 404)
    body = request.get_json()
    if not ("name" in body):
        raise APIException("keyError: name", 404)
    if not ("eye_color" in body):
        raise APIException("keyError: eye_color", 404)
    if not ("birthday_date" in body):
        raise APIException("keyError: birthday_date", 404)
    if not ("gender" in body):
        raise APIException("keyError: gender", 404)
    if not ("height" in body):
        raise APIException("keyError: height", 404)
    
    character.name = body["name"]
    character.eye_color = body["eye_color"]
    character.birthday_date = body["birthday_date"]
    character.gender = body["gender"]
    character.height = body["height"]
    db.session.commit()
    return jsonify(character.serialize()), 200

# Obtener un solo personaje
@app.route('/character/<int:character_id>', methods=['GET'])
def get_detail_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        raise APIException("Personaje no encontrado", 404)
    return jsonify(character.serialize()),200

# Eliminar un solo personaje
@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        raise APIException("Personaje no encontrado", 404)
    db.session.delete(character)
    db.session.commit()
    return jsonify("Personaje eliminado", character.serialize()),200
# # FIN PERSONAJES

# INICIO USUARIOs
@app.route('/user', methods=['GET'])
def get_all_users():

    users = User.query.all()
    all_users = list(map(lambda user: user.serialize(), users))

    return jsonify(all_users), 200

@app.route('/user/register', methods=['POST'])
def create_user():
   
    body = request.get_json()
    user = User(email=body["email"], is_active=True, password="****")
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException("Usuario no encontrado", 404)
    return jsonify(user.serialize()), 200
# FIN USUARIOS

# INICIO FAVORITOS
# Obtener favoritos
@app.route('/user/favorites', methods=['GET'])
def get_user_favorites():
    favorites = Favorite.query.all()
    all_favorites = list(map(lambda favorite: favorite.serialize(), favorites))

    return jsonify(all_favorites), 200

# Añadir un nuevo planeta favorito al usuario actual
@app.route('/favorites/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    body = request.get_json()
    favorite_planet = Favorite(user_id=body["user_id"], planet_id=planet_id)
    db.session.add(favorite_planet)
    db.session.commit()
    return jsonify("Planeta favorito añadido"), 201

# Añadir un nuevo personaje favorito al usuario actual
@app.route('/favorites/character/<int:character_id>', methods=['POST'])
def add_favorite_character(character_id):
    body = request.get_json()
    favorite_character = Favorite(user_id=body["user_id"], character_id=character_id)
    # if character_id is None:
    #     raise APIException("Personaje no encontrado", 404)
    db.session.add(favorite_character)
    db.session.commit()
    return jsonify("Personaje favorito añadido"), 201

# Eliminar un nuevo planeta favorito al usuario actual
@app.route('/favorites/planet/<int:planet_id>',methods=['DELETE'])
def delete_favorite_planet(planet_id):
    Favorite.query.filter(Favorite.planet_id == planet_id).delete()
    db.session.commit()
    return jsonify("Planeta favorito eliminado"),200

# Eliminar un nuevo personaje favorito al usuario actual
@app.route('/favorites/character/<int:character_id>',methods=['DELETE'])
def delete_favorite_character(character_id):
    Favorite.query.filter(Favorite.character_id == character_id).delete()
    db.session.commit()
    return jsonify("Personaje favorito eliminado"),200
# FIN FAVORITOS

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
