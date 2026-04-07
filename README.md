# 🎬 Re:Genre — Movie Recommendation System

regenreregenre

---

## 🚀 Features

* 🔍 Search any movie from the dataset
* 🎯 Get top similar movie recommendations
* 🖼️ Movie posters fetched dynamically (OMDB API)
* ⚡ FastAPI backend for high performance
* 🎨 Modern, responsive frontend UI
* 🧠 Content-based recommendation using cosine similarity

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Pandas
* Pickle
* Requests
* Python-dotenv

### Frontend

* HTML
* CSS
* JavaScript (Vanilla)

---

## 📂 Project Structure

```
regenre/
│
├── backend/
│   ├── main.py
│   ├── movies.pkl
│   ├── similarity.pkl
│   ├── requirements.txt
│   ├── .env   # (not pushed to GitHub)
│
├── frontend/
│   ├── index.html
│   ├── movies.json
│   ├── interstellar.webp
│
├── .gitignore
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/regenre.git
cd regenre
```

---

### 2️⃣ Backend Setup

```
cd backend
pip install -r requirements.txt
```

Create a `.env` file:

```
OMDB_API_KEY=your_api_key_here
```

Run the server:

```
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup

Open `frontend/index.html` in your browser.

OR use Live Server in VS Code.

---

## 🔌 API Endpoint

### Get Recommendations

```
GET /recommend?movie=MovieName
```

Example:

```
http://127.0.0.1:8000/recommend?movie=Avatar
```

---

## 🧠 How It Works

* Movies are vectorized using text features (tags)
* Cosine similarity is used to find similar movies
* Precomputed similarity matrix ensures fast responses
* Posters are fetched dynamically using OMDB API

---

## 🔐 Environment Variables

| Variable     | Description                        |
| ------------ | ---------------------------------- |
| OMDB_API_KEY | API key for fetching movie posters |

---

## ⚠️ Notes

* `.env` file is ignored for security
* If API limit exceeds, posters may not load
* Dataset must contain exact movie names

---

## 📌 Future Improvements

* User authentication
* Watchlist feature
* Add TMDB fallback API
* Better recommendation filtering

---

## 🙌 Acknowledgements

* OMDB API for movie posters
* FastAPI for backend framework

---

## ⭐ Show some love

If you like this project, give it a ⭐ on GitHub!

---
