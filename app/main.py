import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title = 'Remove Background')

st.title("Remove Background")

menu = ['Webcam','Select Image','About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Webcam':
    st.subheader("Capture a Image using webcam")

elif choice == 'Select Image':
    st.subheader("Upload Your Image")

elif choice == 'About':
    st.subheader("About page")