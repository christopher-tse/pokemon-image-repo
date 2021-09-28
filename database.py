
import sqlite3
import os
import pandas


def init_db():
    conn, curs = db_handlers()

    # wipe/reset database if table exists
    conn.execute("DROP TABLE IF EXISTS pokedex")
    
    conn.execute("CREATE TABLE pokedex (name TEXT, type1 TEXT, type2 TEXT, src TEXT, path TEXT)")

    # update jpg files from dataset to have png extension
    # referenced from https://stackoverflow.com/questions/16736080/change-the-file-extension-for-files-in-a-folder
    folder = './static/images'
    for filename in os.listdir(folder):
        infilename = os.path.join(folder, filename)
        if not os.path.isfile(infilename): continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace('.jpg', '.png')
        output = os.rename(infilename, newname)

    pokemon_data = pandas.read_csv('./static/pokemon.csv').to_numpy()
    for pokemon in pokemon_data:
        name = pokemon[0].upper()
        type1 = pokemon[1].upper() if not isinstance(pokemon[1], float) else "--"
        type2 = pokemon[2].upper() if not isinstance(pokemon[2], float) else "--"
        src = pokemon[0] + ".png"
        path = "/static/images/" + pokemon[0] + ".png"
        data_tuple = (name, type1, type2, src, path)
        curs.execute("INSERT INTO pokedex (name, type1, type2, src, path) VALUES (?, ?, ?, ?, ?)", data_tuple)

    conn.commit()


def db_handlers():
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()

    return conn, curs