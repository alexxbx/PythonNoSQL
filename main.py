# pprint library is used to make the output look more pretty
from flask import Flask
from flask import request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import make_response
import json
from pymongo import MongoClient
import random



# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

app = Flask(__name__)

app.secret_key = "secret_key"

#client = MongoClient("mongodb+srv://admin:admin@animeproject.no3y7.mongodb.net/<AnimeProject?retryWrites=true&w=majority")

app.config['MONGO_URI'] = "mongodb+srv://admin:admin@animeproject.no3y7.mongodb.net/AnimeProject?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_anime():
    _json = request.json
    _name = _json['anime_title']
    _episodes = _json['anime_num_episodes']

    if _name and _episodes and request.method == 'POST':

        id = mongo.db.anime.insert_one({'anime_title': _name, 'anime_num_episodes': _episodes})

        resp = jsonify("Anime added successfully")

        resp.status_code = 200

        return resp

    else:
        return not_found()


@app.route('/project', methods=['GET'])
def animes():
    animes = mongo.db.anime.find()
    resp = dumps(animes)
    return resp

@app.route('/project/<id>')
def anime(id):
    anime = mongo.db.anime.find_one({'_id':ObjectId(id)})
    resp = dumps(anime)
    return resp

@app.route('/delete/<id>', methods=['DELETE'])
def delete_anime(id):
    mongo.db.anime.delete_one({'_id': ObjectId(id)})
    resp = jsonify("Anime deleted successfully")

    resp.status_code = 200

    return resp

@app.route('/update/<id>', methods=['PUT'])
def update_anime(id):
    _id = id
    _json = request.json
    _name = _json['anime_title']
    _episodes = _json['anime_num_episodes']

    if _name and _episodes and _id and request.method == 'PUT':
        mongo.db.anime.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'anime_title': _name, 'anime_num_episodes': _episodes}})

        resp = jsonify("Anime updated successfully")

        resp.status_code = 200

        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message':'Not Found :' + request.url
    }
    resp = jsonify(message)

    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(debug=True)





