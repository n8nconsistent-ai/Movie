# 🎬 Movie Recommendation System

A **content-based Movie Recommendation System** built using **Python, Machine Learning, and Streamlit** that suggests movies based on similarity matching.

---

## 🚀 Live Features

✅ Movie recommendation using similarity score
✅ Genre-based filtering
✅ Interactive search bar
✅ Netflix-style UI using Streamlit
✅ Fast recommendation engine using cosine similarity

---

## 📌 Project Overview

This project recommends movies similar to the one selected by the user using **content-based filtering**.

The recommendation system analyzes movie metadata such as:

* Genres
* Keywords
* Cast
* Crew
* Overview

and computes similarity between movies using machine learning techniques.

---

## 🧠 Machine Learning Concept Used

* Content-Based Recommendation
* Text Vectorization
* Cosine Similarity
* Data Preprocessing using Pandas & NumPy

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Matplotlib

---

## 📂 Project Structure

```
movie/
│
├── app.py                 # Streamlit Application
├── movies.pkl             # Movie dataset
├── similarity.pkl         # Similarity matrix (Large file)
├── background.jpeg        # UI Background image
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚠️ Important Note (Large File)

The file **similarity.pkl (~814MB)** exceeds GitHub's upload limit.

Therefore, it is hosted externally.

👉 Download it from Google Drive:

🔗 **DOWNLOAD LINK:**
https://drive.google.com/file/d/1ieuqfUuTqoMMTJXLmBrHXF1jLqV6AIOA/view?usp=sharing

After downloading:

Place the file inside the project folder:

```
movie/similarity.pkl
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/n8nconsistent-ai/Movie.git
cd Movie
```

---

### 2️⃣ Create Virtual Environment

```
conda create -n movie python=3.10
conda activate movie
```

(or)

```
python -m venv movie
movie\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Download similarity.pkl

Download from Google Drive link provided above and place it inside the project folder.

---

### 5️⃣ Run Application

```
streamlit run app.py
```

---

## 🎥 Application Preview

Netflix-style interface with intelligent movie suggestions.

---

## 📈 Future Improvements

* Movie posters using TMDB API
* User login system
* Hybrid recommendation system
* Cloud deployment
* Real-time search suggestions

---


## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
