import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    color: white;
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

.title { text-align:center;font-size:42px;font-weight:bold;color:#f5f5f5;animation:fadeInDown 1s ease-in-out; }
.card {
    background-color: rgba(255,255,255,0.1);
    padding: 1.5rem;
    border-radius: 12px;
    margin-bottom: 1rem;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: #ffffff !important;
}
.stMarkdown, .stText, .stSubheader, .stHeader, .stWrite {
    color: #ffffff !important;
}

.button {
    background-color:#e94560;color:white;padding:0.8rem 1.5rem;border:none;border-radius:10px;font-size:18px;cursor:pointer;
    transition:transform 0.3s ease-in-out;
}
.button:hover { transform:scale(1.05); }
@keyframes fadeInDown {
    from {opacity:0;transform:translateY(-20px);}
    to {opacity:1;transform:translateY(0);}
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>⚙️ Settings</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'><h3>🎧 Audio Settings</h3>", unsafe_allow_html=True)
    volume = st.slider("Voice Volume", 0, 100, 70)
    language = st.selectbox("Language", ["English", "Hindi", "Tamil", "Telugu"])
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'><h3>🎯 Detection Settings</h3>", unsafe_allow_html=True)
    sensitivity = st.slider("Detection Sensitivity", 1, 10, 5)
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'><h3>✨ Upcoming Features</h3><ul><li>Custom voice tones</li><li>Vibration-based feedback</li><li>Indoor mapping</li></ul></div>", unsafe_allow_html=True)

if st.button("💾 Save Settings"):
    st.success(f"Settings saved! Volume: {volume}, Sensitivity: {sensitivity}, Language: {language}")

st.page_link("pages/3_Help.py", label="🚀 Help Needed??", icon="🧭")
