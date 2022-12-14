import streamlit as st
import numpy as np
from utils import webcam, upload_image, before_after, apply_selfie_segmentation
from PIL import Image, ImageEnhance
import os

def main():

    st.set_page_config(page_title = 'Remove Background')

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    st.title("Remove Background")

    path = os.path.dirname(__file__)
    icon = path+'/assets/icon.png'
    # print(icon)

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
        st.image(image, width=100)

    # Add a header and expander in side bar
    st.sidebar.markdown('<p class="font">Remove backgrounds</p>', unsafe_allow_html=True)

    menu = ['Upload Image','Use Webcam']
    choice = st.sidebar.selectbox('Menu', menu)



    if choice == 'Upload Image':
        st.subheader("Upload Image")
        uploaded_img = upload_image()

        global output_image
        global output_image_file

        show_output = 0

        col1, col2 = st.columns([0.3, 0.7])

        if uploaded_img:
            with col1:
                remove_bg_btn = st.button("Remove Background")

                # Initialize session state
                if "load_state" not in st.session_state:
                    st.session_state.load_state = False

                if remove_bg_btn or st.session_state.load_state:
                    st.session_state.load_state = True
                    # st.write(my_text)
                    # download = FileDownloader(uploaded_img).download()
                    # with open("flower.png", "rb") as file:

                    segmented_image = apply_selfie_segmentation(uploaded_img)
                    # im = Image.fromarray(segmented_image,"RGB")
                    output_image = segmented_image
                    # print(type(im))
                    im = Image.fromarray(segmented_image)

                    img = im.convert("RGBA")
                    datas = img.getdata()
                
                    newData = []
                
                    for item in datas:
                        if item[0] == 0 and item[1] == 0 and item[2] == 0:
                            newData.append((0, 0, 0, 0))
                        else:
                            newData.append(item)

                    img.putdata(newData)

                    img.save("Edge.png")

                    output_image_file = open("Edge.png", "rb") 

                    show_output = 1

                    # Delete edge.png
            with col2:
                if st.button("Change Background"):
                    uploaded_img = upload_image()
                    
                    segmented_image = apply_selfie_segmentation(uploaded_img)


            # Download & showing output
            if show_output == 1: 
                before_after(uploaded_img,output_image)
                st.success("File ready to download")
                btn = st.download_button(
                                            label="Download Output",
                                            data=output_image_file,
                                            file_name=uploaded_img.name,
                                            mime="image/png"
                                        )
                show_output = 0

    elif choice == 'Use Webcam':
        st.subheader("Capture a Image using webcam")
        uploaded_img = webcam()

        btn = st.download_button(
                        label="Download Output",
                        data=uploaded_img,
                        file_name=uploaded_img.name,
                        mime="image/png"
                    )

    
    with st.sidebar.expander("About the App"):
        st.write("""
            Simple app created by Anup Das as a side project
             to learn Streamlit and computer vision. Hope you enjoy!
        """)

if __name__ == '__main__':
    main()