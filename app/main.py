import streamlit as st
import cv2
import numpy as np
from utils import webcam, upload_image
from PIL import Image, ImageEnhance
import os

def main():
    st.set_page_config(page_title = 'Remove Background')

    st.title("Remove Background")

    path = os.path.dirname(__file__)
    icon = path+'\\assets\\icon.png'
    print(icon)

    image = Image.open(icon)

    # Create two columns with different with
    col1, col2 = st.columns([0.8, 0.2])
    
    #display header text using css style
    with col1:
        st.markdown("""
        <style>.font {
            font-size:35px; font-family:'Cooper Black'; color:#FF9633;
        }
        </style>
        """, unsafe_allow_html = True)
        st.markdown('<p class="font">Upload your photo here.</p>', unsafe_allow_html = True)
    
    with col2:
        st.image(image, width=150)

    menu = ['Select Image','Webcam','About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Select Image':
        st.subheader("Upload Your Image")
        uploaded_img = upload_image()
        
        if st.button("Remove Background"):
            # st.write(my_text)
            # download = FileDownloader(uploaded_img).download()
            # with open("flower.png", "rb") as file:
            btn = st.download_button(
                        label="Download Output",
                        data=uploaded_img,
                        file_name=uploaded_img.name,
                        mime="image/png"
                    )

    elif choice == 'Webcam':
        st.subheader("Capture a Image using webcam")
        uploaded_img = webcam()

        btn = st.download_button(
                        label="Download Output",
                        data=uploaded_img,
                        file_name=uploaded_img.name,
                        mime="image/png"
                    )

    elif choice == 'About':
        st.subheader("About page")

if __name__ == '__main__':
    main()