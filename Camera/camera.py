import streamlit as st
from PIL import Image
import pandas as pd


def make_grey(photo):
    photo = Image.open(photo)
    gray_scale = photo.convert("L")
    return gray_scale


with st.expander("Camera"):
    camera_image = st.camera_input("Smile!")

if camera_image:
    camera_image = make_grey(camera_image)
    st.image(camera_image)
    print(camera_image)

with st.expander("Upload JPEG only"):
    uploaded_image = st.file_uploader("Upload your file")

if uploaded_image:

    uploaded_image = make_grey(uploaded_image)
    st.image(uploaded_image)

