import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Indian Movie Dataset ---
data = {
    "movie": [
        "3 Idiots", "Dangal", "PK", "Bahubali", "KGF", "RRR",
        "Kabir Singh", "Drishyam", "Drishyam 2", "Kantara",
        "Chennai Express", "War", "Singham", "Sooryavanshi",
        "Padmaavat", "Gully Boy", "Brahmastra", "Sita Ramam",
        "Jawan", "Pathaan"
    ],
    "genre": [
        "Drama Comedy", "Drama Sports", "Comedy Drama", "Action Fantasy",
        "Action Drama", "Action Drama", "Drama Romance", "Thriller Drama",
        "Thriller Drama", "Action Thriller", "Comedy Action Romance",
        "Action Thriller", "Action Drama", "Action Thriller", "Historical Drama",
        "Drama Musical", "Action Fantasy", "Romance Drama", "Action Thriller",
        "Action Thriller"
    ]
}

df = pd.DataFrame(data)

# --- Vectorize Genres ---
vectorizer = CountVectorizer()
matrix = vectorizer.fit_transform(df['genre'])

# --- Similarity Matrix ---
similarity = cosine_similarity(matrix)

def recommend(movie_name):
    movie_name = movie_name.title()

    if movie_name not in df['movie'].values:
        print("\nMovie not found in database!")
        return
    
    index = df[df['movie'] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommendations similar to '{movie_name}':")
    for i, score in scores[1:6]:
        print("•", df['movie'][i])

# --- USER INPUT ---
user_input = input("Enter a movie name: ")
recommend(user_input)
