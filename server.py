from flask import Flask
from DeepImageSearch import Index, LoadData, SearchImage
from flask.templating import render_template


import os
import database


app = Flask(__name__)


@app.route("/searchByType/<string:type1>/<string:type2>")
def searchByType(type1, type2):
    _, curs = database.db_handlers()
    curs.execute("SELECT * FROM pokedex WHERE type1 = ? AND type2 = ?", (type1, type2,))

    pokemon_list = []
    for res in curs.fetchall()[0:19]:
        pokemon_list.append({
            "name": res[0],
            "type1": res[1],
            "type2": res[2],
            "path": res[4]
        })

    return render_template("results.html", pokemon_list = pokemon_list)


@app.route("/searchByImage/<src>")
def searchByImage(src):
    _, curs = database.db_handlers()

    pokemon_dict = SearchImage().get_similar_images(image_path = "./static/images/" + src, number_of_images = 20)
    pokemon_list = []
    for path in pokemon_dict.values():
        # truncate new image path without root spec (.)
        path = path[1:]

        curs.execute("SELECT * FROM pokedex WHERE path = ?", (path,))
        res = curs.fetchone()

        pokemon_list.append({
            "name": res[0],
            "type1": res[1],
            "type2": res[2],
            "path": res[4]
        })

    return render_template("results.html", pokemon_list = pokemon_list)


@app.route('/')
def landing():
    _, curs = database.db_handlers()
    curs.execute("SELECT * FROM pokedex")

    pokemon_list = []
    for res in curs.fetchall()[0:19]:
        pokemon_list.append({
            "name": res[0],
            "type1": res[1],
            "type2": res[2],
            "src": res[3],
            "path": res[4]
        })

    return render_template("landing.html", pokemon_list = pokemon_list)


@app.before_first_request
def before_first_request_func():
    database.init_db()

    folder = ['./static/images']
    image_list = LoadData().from_folder(folder)

    # indexing metadata - initial run will take a bit longer
    # for development comment out coditional statement to update meta-data-files
    if not os.path.isdir('./meta-data-files'):
        Index(image_list).Start()