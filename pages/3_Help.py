import streamlit as st

st.set_page_config(page_title="Help", layout="wide")

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
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
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

st.markdown("<h1 class='title'>❓ Help & Support</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>🧭 Using LightPath</h3>
<ol>
<li>Go to <b>Live Navigation</b> to start camera guidance.</li>
<li>Choose <b>Set Destination</b> or use current environment.</li>
<li>Allow permissions for camera and microphone.</li>
<li>Follow voice commands for movement.</li>
<li>Adjust preferences in <b>Settings</b>.</li>
</ol>
</div>

<div class='card'>
<h3>📞 Contact & Support</h3>
<p>Email: support@lightpath.ai<br>Phone: +91 98765 43210<br>Website: www.lightpath.ai</p>
</div>

<div class='card'>
<h3>💡 About</h3>
<p>LightPath is an AI-powered system developed to empower visually impaired individuals for independent navigation.</p>
</div>


""", unsafe_allow_html=True)
st.page_link("app.py", label="🚀 Go Back To Home", icon="🧭")

