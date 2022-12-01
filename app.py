# Import Libraries
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

# Streamli
import streamlit as st

from PIL import Image

import torch

from torchvision import transforms



st.title('Image App')

#######
def loadModel(m):
    model = torch.load(m)
    model.eval()
    return model

def predict(model,image):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    img = Image.open(image)
    convert_tensor = transforms.ToTensor()
    inputs = convert_tensor(img)
    inputs = inputs.to(device)
    inputs = inputs.unsqueeze(0)
    outputs = model(inputs)
    
    _, preds = torch.max(outputs, 1)

    return preds

bonsai_list = ['Bunjinji',
 'Chokkan',
 'Fukinagashi',
 'Han Kengai',
 'Hokidachi',
 'Moyogi',
 'Seki-joju',
 'Sokan',
 'Yose-ue']

 
def getClass(preds,class_list):
    return class_list[preds[0]]



#######

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

    data = st.radio(
        "image data",
        ('dogsvscats', 'bonsai','cifar10','cifar100'))

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

st.write('Selection summary')

params = {
    'img': image_file,
    'task': task,
    'data': data,
    'model': option
}

st.write(params)

if st.button('Predict'):
    model = loadModel('./models/bonsai/model_ss.pt')
    result = predict(model,image_file[0])
    class1 = getClass(result,bonsai_list)
    st.write(class1)