import streamlit as st

image = st.file_uploader("select image")
st.image(image)