# pprint library is used to make the output look more pretty
from flask import Flask
from flask import request
from flask import make_response
import json
from pymongo import MongoClient
import random
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient("mongodb+srv://admin:admin@animeproject.no3y7.mongodb.net/<AnimeProject?retryWrites=true&w=majority")
db=client["project"]
col = db["anime"]

names = ['Naruto','One Piece']
genre = ['Shonen', 'Seinen']

for x in range(1, 501):
    project = {
        'name' : names[1],
        'rating' : random.randint(1, 5),
        'genre' : genre[0]
   }

x = col.find({}, {'anime_title': 'Chihayafuru'})
for data in x:
    print(data)
#result=db.anime.insert_one(project)
#print('Created an anime'.format(x,result.inserted_id))

#Step 5: Tell us that you are done

#print('finished creating :' + names[1])



app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def acceuil():
    """la fonction ouvre le fichier JSON afin de récupérer ce qu'il se trouve"""

    if request.method == "GET":
        #id = request.args["id"]
        with open('.json') as mon_fichier:
            data = mon_fichier.read()
        return make_response(data ,200)

    elif request.method == "POST":
        id = request.args["id"]
        with open(id+'.json', 'w') as mon_fichier:
            json.dump(request.get_json(), mon_fichier)
        return make_response("ok", 200)


if (__name__) == '__main__':
    app.run(
        host="10.138.33.247",
        port=8081,
        debug=True,
    )