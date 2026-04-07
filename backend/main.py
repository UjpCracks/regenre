from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import pickle
import requests
from fastapi.middleware.cors import CORSMiddleware
import gdown 

import os
from dotenv import load_dotenv
load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Google Drive file IDs
MOVIES_ID = "1rwSshri0uidS_INCGS7iEybUsmJIQavN"          # replace with your movies.pkl Google Drive ID
SIMILARITY_ID = "1-ZKkVdV4vUyzYbSXI6aU74zuR5c9aspZ"  # replace with your similarity.pkl Google Drive ID

# Local filenames
MOVIES_FILE = "movies.pkl"
SIMILARITY_FILE = "similarity.pkl"

# Download if missing
if not os.path.exists(MOVIES_FILE):
    gdown.download(f"https://drive.google.com/uc?id={MOVIES_ID}", MOVIES_FILE, quiet=False)
if not os.path.exists(SIMILARITY_FILE):
    gdown.download(f"https://drive.google.com/uc?id={SIMILARITY_ID}", SIMILARITY_FILE, quiet=False)
# Load pickle files
movies = pickle.load(open(MOVIES_FILE, 'rb'))
similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))



def fetch_poster(movie_name):
    try:
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={movie_name}"
        data = requests.get(url, timeout=5).json()
        poster = data.get("Poster")
        if poster and poster != "N/A":
            return poster
        
    except Exception:
        pass

    return "https://via.placeholder.com/300x450?text=No+Image"


def recommend(movie):
    matches = movies[movies['title'].str.lower() == movie.strip().lower()]
    if matches.empty:
        return None
    movie_index = matches.index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:5]
    recommended_movies = []

    # 🔥 Add searched movie FIRST (manually)
    recommended_movies.append({
        "title": movie,
        "poster": fetch_poster(movie)
    })

    for i in movies_list:
        title = movies.iloc[i[0]].title
        poster = fetch_poster(title)
        recommended_movies.append({"title": title, "poster": poster})
    return recommended_movies


# Handles: GET /recommend?movie=Avatar
@app.get("/recommend")
def get_recommendation_query(movie: str):
    results = recommend(movie)
    if results is None:
        raise HTTPException(status_code=404, detail=f"Movie '{movie}' not found.")
    return {"results": results}


# Handles: GET /recommend/Avatar  (old path style, kept for compatibility)
@app.get("/recommend/{movie:path}")
def get_recommendation_path(movie: str):
    results = recommend(movie)
    if results is None:
        raise HTTPException(status_code=404, detail=f"Movie '{movie}' not found.")
    return {"results": results}



