import streamlit as st
‎import random
‎
‎st.set_page_config(page_title="Wingo Predictor", layout="centered")
‎
‎# Custom CSS for styling
‎st.markdown("""
‎    <style>
‎        .main {
‎            background-color: white;
‎            padding: 30px;
‎            border-radius: 10px;
‎            box-shadow: 2px 2px 10px #ccc;
‎        }
‎        .stButton > button {
‎            background-color: #4CAF50;
‎            color: white;
‎            font-size: 16px;
‎            border-radius: 8px;
‎            height: 3em;
‎            width: 100%;
‎        }
‎    </style>
‎""", unsafe_allow_html=True)
‎
‎st.title("🎯 Wingo AI Color Predictor")
‎st.markdown("<h4 style='text-align: center; color: grey;'>Smart AI-Based Prediction for Wingo</h4>", unsafe_allow_html=True)
‎st.markdown("Aakhri 3 numbers daalein:")
‎
‎def get_color(number):
‎    if number in [1, 3, 7, 9]:
‎        return "Red"
‎    elif number in [0, 2, 4, 6, 8]:
‎        return "Green"
‎    elif number == 5:
‎        return "Violet"
‎
‎n1 = st.number_input("Number 1", 0, 9, step=1)
‎n2 = st.number_input("Number 2", 0, 9, step=1)
‎n3 = st.number_input("Number 3", 0, 9, step=1)
‎
‎if 'history' not in st.session_state:
‎    st.session_state.history = []
‎
‎if st.button("🔮 Predict"):
‎    colors = [get_color(n) for n in [n1, n2, n3]]
‎    prediction = random.choice(["Red", "Green", "Violet"])
‎    st.session_state.history.append((colors, prediction))
‎
‎    st.success(f"Prediction: {prediction}")
‎    st.info(f"Pattern: {colors}")
‎
‎if st.session_state.history:
‎    st.subheader("📜 Previous Predictions:")
‎    for idx, (pattern, result) in enumerate(reversed(st.session_state.history[-5:]), 1):
‎        st.write(f"{idx}. Pattern: {pattern} → Prediction: {result}")
