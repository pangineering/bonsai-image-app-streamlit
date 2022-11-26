# Import Libraries
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

# Streamli
import streamlit as st

from PIL import Image

import torch

st.title('Image App')




st.header('Image Form')

def load_image(image_file):
	img = Image.open(image_file)
	return img



st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"],accept_multiple_files=True)

if image_file is not None:
	
	result = []

	# To View Uploaded Image
	for img_file in image_file:
		img = load_image(img_file)
		
		st.image(img,width=200)

st.subheader("Task")
task = st.selectbox(
    'Select a task',
    ('image classification', 'object recognition', 'image segmentatiom'),key=2)

st.write('You selected:', task)

if task == 'image classification':
    classification = st.radio(
        "image classification",
        ('binary', 'multi'))

# if genre == 'Comedy':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn't select comedy.")

st.subheader("Models")
option = st.selectbox(
    'Select a model',
    ('Model1', 'Model2', 'Model3'))

st.write('You selected:', option)