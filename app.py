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

    data = st.radio(
        "image data",
        ('dogsvscats', 'bonsai','cifar10','cifar100'))

# if genre == 'Comedy':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn't select comedy.")
if task == 'image classification':
    models = ('Model1', 'Model2', 'Model3')
elif task == 'object recognition':
    models = ('Model4', 'Model5', 'Model6')
else:
    models = ('Model7', 'Model8', 'Model9')
    
        
st.subheader("Models")
option = st.selectbox(
    'Select a model',
    models)

st.write('You selected:', option)