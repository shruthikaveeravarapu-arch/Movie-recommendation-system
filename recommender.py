"""Original educational content-based movie recommender (Python standard library)."""
import csv
import math
import re
from collections import Counter
from pathlib import Path

DATA_PATH = Path(__file__).with_name('movies.csv')


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def load_movies(path=DATA_PATH):
    with open(path, newline='', encoding='utf-8') as stream:
        movies = list(csv.DictReader(stream))
    required = {'title', 'genres', 'keywords', 'description'}
    if not movies or not required.issubset(movies[0]):
        raise ValueError('Movie CSV is empty or missing required columns')
    return movies


def movie_text(movie):
    # Weight genres twice to make explicit genre preferences matter more.
    return ' '.join([movie['genres'], movie['genres'], movie['keywords'], movie['description']])


def vectors_for(movies, query):
    documents = [tokenize(movie_text(movie)) for movie in movies] + [tokenize(query)]
    df = Counter(token for doc in documents for token in set(doc))
    n = len(documents)
    vectors = []
    for doc in documents:
        counts = Counter(doc)
        vec = {word: (1 + math.log(freq)) * (math.log((1 + n) / (1 + df[word])) + 1)
               for word, freq in counts.items()}
        length = math.sqrt(sum(value * value for value in vec.values()))
        vectors.append({word: value / length for word, value in vec.items()} if length else {})
    return vectors


def recommend(query, movies=None, top_n=5, exclude_title=None):
    """Return ranked (score, movie) pairs for a preference phrase."""
    if not query or not query.strip():
        raise ValueError('Enter at least one preference keyword')
    if top_n < 1:
        raise ValueError('top_n must be positive')
    movies = load_movies() if movies is None else movies
    if not movies:
        return []
    vectors = vectors_for(movies, query)
    target = vectors[-1]
    ranked = []
    for movie, vector in zip(movies, vectors[:-1]):
        if exclude_title and movie['title'].casefold() == exclude_title.casefold():
            continue
        score = sum(value * target.get(word, 0) for word, value in vector.items())
        ranked.append((score, movie))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]['title']))
    return [(score, movie) for score, movie in ranked if score > 0][:top_n]


if __name__ == '__main__':
    from app import main
    main()
