import streamlit as slt
import pickle
import base64

# Page Config
slt.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("background.jpeg")

# Custom CSS
slt.markdown(f"""
<style>

/* Remove padding */
.block-container {{
    padding: 0rem;
}}

/* HERO IMAGE CONTAINER */
.hero {{
    position: relative;
    width: 100%;
    height: 700px;
    background-image: url("data:image/jpeg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    border-radius: 8px;
}}

/* Dark overlay */
.hero::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.6);
    border-radius: 8px;
}}

/* TEXT OVER IMAGE */
.hero-content {{
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: white;
    width: 70%;
    z-index: 2;
}}

.hero-content h1 {{
    font-size: 3rem;
    font-weight: 800;
}}

.hero-content p {{
    font-size: 1.1rem;
    color: #ddd;
}}

/* Button */
.stButton>button {{
    background-color: #e50914;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    padding: 10px 25px;
    border: none;
}}

.stButton>button:hover {{
    background-color: #f6121d;
}}

/* Pull FILTER row up */
div[data-testid="stHorizontalBlock"]:nth-of-type(1) {{
    margin-top: -420px;
    position: relative;
    z-index: 10;
}}

/* Pull SEARCH row up */
div[data-testid="stHorizontalBlock"]:nth-of-type(2) {{
    margin-top: -20px;
    position: relative;
    z-index: 10;
}}

/* Dropdown style */
div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-baseweb="select"] > div,
div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-baseweb="select"] > div {{
    background-color: rgba(0,0,0,0.6);
    color: white;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 6px;
}}

div[data-testid="stHorizontalBlock"]:nth-of-type(1) span,
div[data-testid="stHorizontalBlock"]:nth-of-type(2) span {{
    color: white !important;
}}

/* SEARCH ICON */
.search-box {{
    position: relative;
}}


</style>
""", unsafe_allow_html=True)

# Load Data
df = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Genres
all_genres = sorted(set(g for x in df['genres'] for g in x.split('|')))

def recommend(movie_name, base_df):
    index = df[df['title'] == movie_name].index[0]
    scores = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, _ in scores:
        title = df.iloc[i]['title']
        if title != movie_name and title in base_df['title'].values:
            recommendations.append(title)
        if len(recommendations) == 5:
            break

    return recommendations

# Hero
slt.markdown("""
<div class="hero">
    <div class="hero-content">
        <h1>Unlimited Movies,<br> Personalized for You</h1>
        <p>Discover movies using intelligent similarity matching</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Filter
_, _, col3 = slt.columns([6,1,1])
with col3:
    selected_genre = slt.selectbox("", ["All"] + all_genres, label_visibility="collapsed")

filtered_df = df if selected_genre == "All" else df[df['genres'].str.contains(selected_genre)]

# Search
_, col_b, _ = slt.columns([1, 2, 1])

with col_b:
    movie = slt.text_input(
        "",
        placeholder="🔍 Search movie here"
    )

    if slt.button("Recommend", use_container_width=True):
        slt.session_state["show"] = True

# ================= SHOW RESULTS =================

if slt.session_state.get("show") and movie:

    if selected_genre != "All" and movie not in filtered_df['title'].values:
        slt.warning("Selected movie does not belong to the chosen genre.")

    else:
        slt.markdown("## 🎬 Recommended Movies")
        recommendations = recommend(movie, filtered_df)

        for m in recommendations:
            slt.markdown(
                f"<div style='background:#111;padding:15px;margin-bottom:10px;border-radius:5px;color:white;'>{m}</div>",
                unsafe_allow_html=True
            )