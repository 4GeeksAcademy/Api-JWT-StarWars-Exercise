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
from models import db, Users, People, Planets, Starships, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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

# PEOPLE

@app.route('/people', methods=['GET'])
def get_all_people():
    query_results = People.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
 
    print(query_results)
    
    if results != []:
        response_body = {
        "msg": "OK",
        "results": results
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": "There aren't any people yet"}), 404



@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):
    query_results = People.query.filter_by(id=people_id).first()
 
    print(query_results)
    
    if query_results is not None:
        response_body = {
        "msg": "OK",
        "results": query_results.serialize()
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": f"People {people_id} not found"}), 404
    

# DELETE ONE PEOPLE

# @app.route('/people/<int:people_id>', methods=['DELETE'])
# def delete_one_people(people_id):
#     query_results = People.query.filter_by(id=people_id).first()
 
#     print(query_results)
    
#     if query_results is not None:
#         response_body = {
#         "msg": "OK",
#         "results": query_results.serialize()
#     }
#         return jsonify(response_body), 200
    
#     else:
#         return jsonify({"msg": f"People {people_id} not found"}), 404
    


# PLANETS

@app.route('/planets', methods=['GET'])
def get_all_planets():
    query_results = Planets.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
 
    print(query_results)
    
    if results != []:
        response_body = {
        "msg": "OK",
        "results": results
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": "There aren't any planets yet"}), 404



@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_one_planet(planets_id):
    query_results = Planets.query.filter_by(id=planets_id).first()
 
    print(query_results)
    
    if query_results is not None:
        response_body = {
        "msg": "OK",
        "results": query_results.serialize()
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": f"Planets {planets_id} not found"}), 404

# STARSHIPS

@app.route('/starships', methods=['GET'])
def get_all_starships():
    query_results = Starships.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
 
    print(query_results)
    
    if results != []:
        response_body = {
        "msg": "OK",
        "results": results
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": "There aren't any starships yet"}), 404



@app.route('/starships/<int:starships_id>', methods=['GET'])
def get_one_starship(starships_id):
    query_results = Starships.query.filter_by(id=starships_id).first()
 
    print(query_results)
    
    if query_results is not None:
        response_body = {
        "msg": "OK",
        "results": query_results.serialize()
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": f"Starship {starships_id} not found"}), 404
    
    
# USERS

@app.route('/users', methods=['GET'])
def get_all_users():
    query_results = People.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
 
    print(query_results)
    
    if results != []:
        response_body = {
        "msg": "OK",
        "results": results
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": "There aren't any users yet"}), 404
    


# GET ALL FAVORITES 
    

@app.route('/users/favorites', methods=['GET'])
def get_all_favorites():
    query_results = Favorites.query.all()
    results = list(map(lambda item: item.serialize(), query_results))
 
    print(query_results)
    
    if results != []:
        response_body = {
        "msg": "OK",
        "results": results
    }
        return jsonify(response_body), 200
    
    else:
        return jsonify({"msg": "There aren't any favorites yet"}), 404
    




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
