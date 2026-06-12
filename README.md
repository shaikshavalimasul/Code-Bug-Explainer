# 🐛 Code Bug Explainer

> An AI-powered web application that explains bugs in your code in plain, simple language — built from scratch with Flask, SQLAlchemy, and real algorithms.

🔗 **Live Demo:** [(https://code-bug-explainer.onrender.com)]

---

## ✨ Overview

Code Bug Explainer lets users paste buggy code in Python, Java, C++, JavaScript, C, or SQL and instantly receive a clear, beginner-friendly explanation of what's wrong and how to fix it — powered by an AI model via the OpenRouter API.

Beyond the AI integration, this project implements **four real algorithms** to solve practical problems: detecting duplicate bugs, searching history efficiently, analyzing coding patterns, and rating bug difficulty.

---

## 🚀 Features

- 🔐 **User Authentication** — secure registration and login with encrypted (hashed) passwords
- 🧠 **AI Bug Explanations** — detailed analysis including what the bug is, why it happens, and how to fix it
- 📜 **Personal Bug History** — each user has their own private history of explained bugs
- 📊 **Statistics Dashboard** — visual breakdown of bugs by language and difficulty
- 🔍 **Smart Search** — instantly filter bug history by programming language
- ♻️ **Duplicate Detection** — recognizes similar past bugs and offers to reuse the explanation (saves API calls)
- 🎯 **Difficulty Rating** — automatically classifies each bug as Easy / Medium / Hard
- 🎨 **Modern, Responsive UI** — glassmorphism-style dark theme

---

## 🧮 Algorithms Implemented

| Algorithm | Purpose | Complexity |
|---|---|---|
| **Frequency Analysis** | Counts bugs per language to generate user statistics | O(n) |
| **Binary Search** | Efficiently searches sorted bug history by language | O(log n) |
| **Levenshtein Distance (DP)** | Detects near-duplicate code submissions via edit distance | O(m×n) |
| **VADER Sentiment Analysis (ML)** | Pre-trained NLP model used to estimate bug difficulty from AI explanation tone | O(1) per call |

---

## 🛠️ Tech Stack

**Backend:** Python, Flask, Flask-SQLAlchemy  
**Database:** MySQL (local development) / SQLite (production)  
**AI:** OpenRouter API (Llama model)  
**Frontend:** HTML, CSS, JavaScript  
**Auth & Security:** Werkzeug password hashing, Flask sessions  
**Deployment:** Render + Gunicorn  
**Version Control:** Git & GitHub

---

## 📂 Project Structure

```
code-bug-explainer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile                # Render deployment config
├── templates/
│   ├── index.html         # Bug explainer page
│   ├── login.html
│   ├── register.html
│   ├── history.html       # Personal bug history with search
│   └── statistics.html    # Analytics dashboard
└── .env                    # Environment variables (not committed)
```

---

## ⚙️ How It Works

```
User submits buggy code
        ↓
Check history with Levenshtein Distance (duplicate?)
        ↓
   Duplicate found?
   ├── Yes → Show previous explanation (instant, free)
   └── No  → Call OpenRouter AI for new explanation
        ↓
VADER analyzes explanation tone → assigns difficulty
        ↓
Save to database (linked to user)
        ↓
Display result + update statistics
```

---

## 🧑‍💻 Run Locally

```bash
# Clone the repo
git clone https://github.com/shaikshavalimasul/Code-Bug-Explainer.git
cd Code-Bug-Explainer

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Add your .env file with:
# OPENROUTER_API_KEY=your_key
# SECRET_KEY=your_secret
# MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

# Run the app
python app.py
```

---

## 📚 What I Learned

Building this project end-to-end taught me:

- REST API design and the request/response cycle (GET vs POST)
- Building a Flask backend with routes, sessions, and authentication
- Database design with relationships (Foreign Keys) using SQLAlchemy ORM
- Secure password storage with hashing
- Integrating third-party AI APIs
- Implementing classic algorithms (Dynamic Programming, Binary Search) in a real product
- Using a pre-trained ML model (VADER) for NLP-based analysis
- Debugging real production errors (database migrations, deployment configs)
- Full deployment pipeline: GitHub → Render → live app

---

## 🙋 About Me

This was my first full-stack project, built step-by-step while learning Python, Flask, SQL, and web development by *doing* — not just watching tutorials.

Feel free to connect or reach out if you have feedback!
