import streamlit as st

st.set_page_config(page_title="LightPath Home", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}
                                
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff, #cfd8ff, #1a1a2e);
    border-right: 2px solid rgba(255,255,255,0.2);
    color: #0f172a;
    font-weight: 500;
}

/* Sidebar Text Color */
[data-testid="stSidebar"] * {
    color: #0f172a !important;
}

/* Optional: make sidebar menu items glow on hover */
[data-testid="stSidebar"] a:hover {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border-radius: 10px;
    transition: 0.3s;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #f5f5f5;
    margin-top: 20px;
    animation: fadeInDown 1s ease-in-out;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #dcdcdc;
    margin-bottom: 40px;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: #ffffff !important;
}
.stMarkdown, .stText, .stSubheader, .stHeader, .stWrite {
    color: #ffffff !important;
}

.card {
    background-color: rgba(255, 255, 255, 0.1);
    padding: 1.5rem;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
}
.feature-box {
    background-color: rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    transition: 0.3s ease-in-out;
}
.feature-box:hover {
    transform: translateY(-5px);
    background-color: rgba(255,255,255,0.15);
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>👣 Welcome to LightPath</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Empowering visually impaired users with real-time AI navigation and voice guidance.</p>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>💡 About LightPath</h3>
<p>LightPath is a smart navigation assistant designed for visually impaired users. It uses AI-powered object detection and voice feedback to guide users safely in both indoor and outdoor environments.</p>
</div>

<div class='card'>
<h3>✨ Core Features</h3>
<div class='feature-grid'>
    <div class='feature-box'>🎯 Real-Time Detection</div>
    <div class='feature-box'>🗣️ Voice Assistance</div>
    <div class='feature-box'>📍 Destination Guidance</div>
    <div class='feature-box'>🎧 Headphone Mode</div>
</div>
</div>



""", unsafe_allow_html=True)
st.page_link("pages/1_Live_Navigation.py", label="🚀 Start Navigation", icon="🧭")

