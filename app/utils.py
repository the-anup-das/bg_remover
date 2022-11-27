import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

import streamlit.components as stc
import base64
import time

# class FileDownloader(object):
	
# 	def __init__(self, data,filename='myfile',file_ext='png'):
# 		super(FileDownloader, self).__init__()
# 		self.data = data
# 		self.filename = filename
# 		self.file_ext = file_ext

# 	def download(self):
# 		b64 = base64.b64encode(self.data.encode()).decode()
# 		new_filename = "{}_{}_.{}".format(self.filename,timestr,self.file_ext)
# 		st.markdown("#### Download File ###")
# 		href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
# 		st.markdown(href,unsafe_allow_html=True)

def load_image(image_file):
    img = Image.open(image_file)
    return img

def webcam():
    img_file_buffer = st.camera_input("Take a picture")

    # @st.cache(suppress_st_warning=True)

    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        # Check the type of cv2_img:
        # Should output: <class 'numpy.ndarray'>
        # st.write(type(cv2_img))

        # Check the shape of cv2_img:
        # Should output shape: (height, width, channels)
        # st.write(cv2_img.shape)
        
        st.image(load_image(img_file_buffer), width = 250)
        return cv2_img

def upload_image():
    st.subheader("Image")
    image_file = st.file_uploader("Upload_file", type = ["png", "jpg", "jpeg"])

    if image_file is not None:
        file_details = {
            'filename': image_file.name,
            'filetype': image_file.type,
            'filesize': image_file.size
        }

        st.write(file_details)

        st.image(load_image(image_file), width = 250)

        # image = Image.open(image_file)

        return image_file

