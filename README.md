# Recommend Me Movies -->

This is a Flask Api which recommend movies similar to the user likes

When you hit this [api](https://recommend-me-movie-h.herokuapp.com/recommend?movie=movie_name) (replace movie_name with movie you want to search). It will recommend top 10 movies based on genres, actors, directors, etc in form of JSON.

In backend machine learning technique called Content Based Filtering is running to filter similar movies using cosine similarity.
