import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Set the input shape
img_height = 224
img_width = 224


# Define a function to preprocess the image
def preprocess_image(image):
    image = image.resize((img_height, img_width))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return image


# Define the class labels
class_names = ['Healthy', 'Diseased']

# Create a Streamlit app
st.title('Plant Disease Classification')

# Create an upload button for the image
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

# Make a prediction if an image has been uploaded
if uploaded_file is not None:
    # Open the image and preprocess it
    image = Image.open(uploaded_file)
    image = preprocess_image(image)

    # Make a prediction and display the result
    prediction = model.predict(image)
    prediction_class = np.argmax(prediction)
    prediction_label = class_names[prediction_class]
    st.write('Prediction:', prediction_label)
    st.image(image[0])
