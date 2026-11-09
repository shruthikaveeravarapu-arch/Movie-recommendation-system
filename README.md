# Movie Match: Content-Based Recommendation System

An original, small educational recommendation system built with the Python standard library. The 30 fictional movie records are original demonstration data, not real ratings or a production catalog.

## Requirements
Python 3.9+; no third-party packages.

## Run
```bash
python app.py
```
Enter `space astronaut mission`, `romance comedy coffee`, or `nature ocean wildlife`. Enter `quit` to stop.

## Tests
```bash
python -m unittest discover -v
```

## Design
Tokenize a doubled-genre + keywords + description document for each movie; compute smoothed IDF and log-scaled TF; L2-normalize TF-IDF vectors; compute cosine similarity by dot product with the user's free-text preferences; rank the top five positive-scoring matches. The interface handles blank queries and no-match results. This is content-based filtering, not a trained neural model or collaborative filtering.

## Source attribution
Original implementation and fictional sample data created for this assignment. Algorithmic concepts informed by the scikit-learn TF-IDF and cosine similarity documentation (https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction and https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity), and the literature cited in the companion report. No external sample source code was copied.

## GitHub submission
Create a repository in your account, upload these files, and replace `[INSERT YOUR GITHUB REPOSITORY URL]` in the report with the real URL. Give your instructor access if the repository is private. Do not claim the upload is complete until verified.

## Limitations
No personal data collection, ratings history, collaborative behavior, semantic embeddings, or offline ranking benchmark. Keyword overlap can miss synonyms and favor longer descriptions.
