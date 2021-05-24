from flask import Flask, request, jsonify
from model.getSimilarMovies import similarMovies


class ApiExeption(Exception):
    code = 400
    description = "Bad Request"

app = Flask('movie_recommendation')

## Flask restful api

@app.errorhandler(ApiExeption)
def handle_exception(err):
   
    # response = {
    #   "error": err.code
    # }
    if len(err.args) > 0:
        # response["message"] = err.args[0]
        response = err.args[0]
    # return jsonify(response), err.code
    return response, err.code

@app.route('/recommend', methods=['GET'])
def recommend():

    movie_name = request.args.get('movie')

    get_similar_movies = similarMovies(movie_name)

    if get_similar_movies is None:

        raise ApiExeption('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')

    else: 

        # response = {    

        #     'movies_1': get_similar_movies[0],
        #     'movies_2': get_similar_movies[1],
        #     'movies_3': get_similar_movies[2],
        #     'movies_4': get_similar_movies[3],
        #     'movies_5': get_similar_movies[4],
        #     'movies_6': get_similar_movies[5],
        #     'movies_7': get_similar_movies[6],
        #     'movies_8': get_similar_movies[7],
        #     'movies_9': get_similar_movies[8],
        #     'movies_10': get_similar_movies[9]
        # }

        response = {

            'movies' : get_similar_movies
            
            }

        return jsonify(response)

if __name__ == '__main__':
    app.run()