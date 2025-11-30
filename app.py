import streamlit as st
import random

st.set_page_config(page_title="Wingo Predictor", layout="centered")

st.title("🔮 Wingo Predictor")
st.markdown("<h5 style='text-align: center; color: grey;'>AI se paayen color prediction ka idea — bas 3 number daalein!</h5>", unsafe_allow_html=True)

def get_color(number):
    if number in [1, 3, 7, 9]:
        return "Red"
    elif number in [0, 2, 4, 6, 8]:
        return "Green"
    elif number == 5:
        return "Violet"

col1, col2, col3 = st.columns(3)

with col1:
    n1 = st.number_input("Number 1", 0, 9, step=1)
with col2:
    n2 = st.number_input("Number 2", 0, 9, step=1)
with col3:
    n3 = st.number_input("Number 3", 0, 9, step=1)
