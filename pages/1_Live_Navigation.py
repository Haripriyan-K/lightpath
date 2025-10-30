import streamlit as st
import cv2
from ultralytics import YOLO
from gtts import gTTS
from playsound import playsound
import threading, os

st.set_page_config(page_title="Live Navigation", layout="wide")

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

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: white;
   
    animation: fadeInDown 1s ease-in-out;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: #ffffff !important;
}
.stMarkdown, .stText, .stSubheader, .stHeader, .stWrite {
    color: #ffffff !important;
}

.card {
    background-color: rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
}
.button {
    background-color: #e94560;
    color: white;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 10px;
    font-size: 18px;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}
.button:hover { transform: scale(1.05); }
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🧭 Live Navigation</h1>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")
model = load_model()

def speak(text):
    def _speak():
        tts = gTTS(text)
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    threading.Thread(target=_speak).start()

st.markdown("<div class='card'>", unsafe_allow_html=True)
mode = st.radio("Choose Mode", ["Use current environment", "Set destination"])
if mode == "Set destination":
    dest = st.text_input("Enter your destination:")
    if dest:
        st.success(f"Destination set to {dest}")
        speak(f"Destination set to {dest}. Starting navigation.")
st.markdown("</div>", unsafe_allow_html=True)

run = st.toggle("Start Navigation")
frame_window = st.empty()

camera = cv2.VideoCapture(0)
while run:
    ret, frame = camera.read()
    if not ret:
        st.error("Camera not found!")
        break
    results = model(frame)
    annotated = results[0].plot()
    boxes = results[0].boxes.xyxy
    dirs = []
    for b in boxes:
        x1, y1, x2, y2 = map(int, b)
        cx = (x1 + x2)//2
        if cx < frame.shape[1]//3:
            dirs.append("left")
        elif cx > 2*frame.shape[1]//3:
            dirs.append("right")
        else:
            dirs.append("center")
    if not dirs:
        cmd = "Path is clear. Move forward."
    elif "center" in dirs:
        cmd = "Stop. Obstacle ahead."
    elif "left" in dirs:
        cmd = "Move right."
    else:
        cmd = "Move left."
    speak(cmd)
    st.markdown(f"<div class='card'><b>🔊 Command:</b> {cmd}</div>", unsafe_allow_html=True)
    frame_window.image(annotated, channels="BGR")
camera.release()

st.page_link("pages/2_Settings.py", label="🚀 GO TO SETTINGS", icon="🧭")

