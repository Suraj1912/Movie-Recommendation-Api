
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset():
    return pd.read_csv('./model/all_movies_dataset.csv')

def similarMovies(movie):

    movie = movie.lower()

    dataset = load_dataset()

    if movie not in dataset['title'].unique():
        return None
    
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(dataset['all_info'])
    cos_sim = cosine_similarity(cv_matrix)

    idx = dataset[dataset['title'] == movie].index[0]  ## get index of movie 

    lst = list(enumerate(cos_sim[idx]))  ## get all cosine similarity list of that index
    lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
    lst = lst[1:11]  ## fetch first 10 most similar movies

    l = []
    for i in range(len(lst)):
        a = lst[i][0]
        l.append(dataset['title'][a])
    
    return l

# print(similarMovies('titanic'))