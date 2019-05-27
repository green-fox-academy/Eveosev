from flask import Flask
from flask import render_template
from flask import jsonify
from flask import make_response
from flask import request
import json

app = Flask(__name__)

movie_data = {}
movie_data[1] = {
    'id': 1,
    'title': 'Warcraft',
    'year': '2016',
    'genre': "Action | Adventure | Fantasy",
    'description': "Looking to escape from his dying world, the orc shaman Gul'dan utilizes dark magic to open a portal to the human realm of Azeroth. Supported by the fierce fighter Blackhand, Gul'dan organizes the orc clans into a conquering army called the Horde. Uniting to protect Azeroth from these hulking invaders are King Llane, the mighty warrior Anduin Lothar (Travis Fimmel) and the powerful wizard Medivh. As the two races collide, leaders from each side start to question if war is the only answer."
}
movie_data[2] = {
    'id': 2,
    'title': 'One Day',
    'year': '2011',
    'genre': "Romance | Drama",
    'description': "On July 15, 1988 -- the day of their college graduation -- two people from opposite sides of the tracks begin a lifelong friendship. Emma (Anne Hathaway), an idealist from a working-class family, wants to make the world a better place. Dexter (Jim Sturgess), a playboy, thinks the world is his oyster. For the next 20 years, the two friends reunite on the 15th of each July, sharing dreams, tears and laughter -- until they discover what they've been searching for, each other."
}

with open('movie_info.txt','w') as m_txt:
    json.dump(movie_data, m_txt)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/movie/<movie_id>')
def LoadMoviePage(movie_id):
    return render_template(f"../static/{movie_id}.html")

@app.route('/api/movies', methods=['GET'])
def get_movies():
    with open('movie_info.txt') as m_txt:
        movie_info = json.load(m_txt)
    response = jsonify(movie_info)
    return response

#Be merged in the later code
# @app.route('/api/<movie_id>')
# def get_movie_byID(movie_id):
#     with open('movie_info.txt') as m_txt:
#         movie_info = json.load(m_txt)
#     response = jsonify(movie_info[str(movie_id)])
#     return response

@app.route('/apimovie')
def apimovie_web():
    return render_template("apimovie.html")

@app.route('/submit_apimovie', methods=["POST"])
def api_verify_apikey():
    API_KEY = request.form.get('API_KEY')
    if API_KEY == '853210':
        return render_template('addmovie.html')
    else:
        response = make_response("error: Invalid API_KEY", 403)
        return response

@app.route('/addmovie')
def add_movie():
    return render_template('addmovie.html')

@app.route('/submit_add_movie', methods=["POST"])
def api_add_movie():
    new_movie_info = {}
# Add new movie info to txt file (in json format)
    with open('movie_info.txt') as m_txt:
        movie_info = json.load(m_txt)
    new_id = len(movie_info) + 1
    new_movie_info = {
        "id": new_id,
        "title": request.form['title'],
        "year": request.form['year'],
        'genre': request.form['genre'],
        'description': request.form['description']
    }
    movie_info[new_id] = new_movie_info
    with open('movie_info.txt', 'w') as m_txt:
        json.dump(movie_info, m_txt)
    response = jsonify(new_movie_info)
    return response

@app.route('/api/movie/<movie_id>', methods=['PUT','DELETE','GET'])
def put_MoviebyID(movie_id):
    if request.method == 'PUT':
        if request.headers['API_KEY'] == '853210':
            with open('movie_info.txt') as m_txt:
                movie_info = json.load(m_txt)
            if movie_id in movie_info:
                new_movie_info = {
                    "id": movie_id,
                    "title": request.form['title'],
                    "year": request.form['year'],
                    'genre': request.form['genre'],
                    'description': request.form['description']
                }
                movie_info[movie_id] = new_movie_info
                with open('movie_info.txt', 'w') as m_txt:
                    json.dump(movie_info, m_txt)   
                response = jsonify(message="replace successfully")
                return response
            else:
                response = jsonify(message=f"No movie in ID {movie_id}, u can add a new one")
                return response
        else:
            response = make_response(f"'error': 'No movie found with {movie_id} ID'", 404)
            return response
    elif request.method == "DELETE":
        if request.headers['API_KEY'] == '853210':
            with open('movie_info.txt') as m_txt:
                movie_info = json.load(m_txt)
            if movie_id in movie_info:
                del movie_info[movie_id]
                with open('movie_info.txt', 'w') as m_txt:
                    json.dump(movie_info, m_txt)   
                response = jsonify(message="Delete successfully")
                return response
            else:
                response = jsonify(message=f"No movie in ID {movie_id}, Please try again"), 404
                return response
        else:
            response = make_response(f"'error': 'No movie found with {movie_id} ID'", 403)
            return response
    elif request.method == 'GET':
        if movie_id in movie_info:
            with open('movie_info.txt') as m_txt:
                movie_info = json.load(m_txt)
            response = jsonify(movie_info[movie_id])
            return response
        else:
            response = jsonify(message=f"No movie in ID {movie_id}, Please try again"), 404
            return response


if __name__ == "__main__":
    app.run()

