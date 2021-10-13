# pprint library is used to make the output look more pretty
from flask import Flask
from flask import request
from flask import make_response
import json
from pymongo import MongoClient
import random
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://admin:admin@animeproject.no3y7.mongodb.net/<AnimeProject?retryWrites=true&w=majority")
db=client.project

names = ['Naruto','One Piece']
genre = ['Shonen', 'Seinen']

for x in range(1, 501):
    project = {
        'name' : names[1],
        'rating' : random.randint(1, 5),
        'cuisine' : genre[0]
    }
result=db.anime.insert_one(project)
print('Created an anime'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating :' + names[1])

app = Flask(__name__)


@app.route("/users", methods=["GET"])

def acceuil():
    """la fonction ouvre le fichier JSON afin de récupérer ce qu'il se trouve"""
    if request.method == "GET":
        with open('user.JSON') as mon_fichier:
            data = json.load(mon_fichier)
        return make_response( "ok",200)

    elif request.method == "POST":
        id = request.args["id"]
        with open(id+'.txt', 'w') as mon_fichier:
            json.dump(request.get_json(), mon_fichier)
        return make_response("ok", 200)


if (__name__) == '__main__':
    app.run(
        host="0.0.0.0",
        port=8081,
        debug=True,
    )