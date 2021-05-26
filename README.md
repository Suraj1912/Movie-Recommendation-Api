# Recommend Me Movies -->

This is a Flask Api which recommend movies similar to the user likes

When you hit this [api](https://recommend-me-movie-h.herokuapp.com/recommend?movie=movie_name) (replace movie_name with movie you want to search). It will recommend top 10 movies based on genres, actors, directors, etc in form of JSON.

In backend machine learning technique called Content Based Filtering is running to filter similar movies using cosine similarity.

## Datasets ->

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. Also Data was taken from WikiPedia
