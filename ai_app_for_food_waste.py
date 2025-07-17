import streamlit as st
#import tensorflow as tf
import numpy as np
from PIL import Image
import requests
import io

# Teachable Machine model URL (from user)
MODEL_URL = "https://teachablemachine.withgoogle.com/models/kTscCbcH0/"
MODEL_JSON = MODEL_URL + "model.json"

# App title and description
st.set_page_config(page_title="AI Food Waste Classifier", layout="centered")
st.title("🍎 AI Food Waste Awareness System")
st.markdown("""
### SDG 12 – Responsible Consumption and Production
This AI tool classifies food images as **Fresh**, **Leftover**, or **Spoiled** to raise awareness and reduce waste.
""")

# Load model using TensorFlow.js-compatible model URL (requires custom handling)
st.info("Note: Due to Streamlit limitations, direct loading from Teachable Machine hosted models via TFJS is not supported natively in Python. For live demos, convert and download the model.")
st.warning("This app is a placeholder showing how the UI will look. To make it functional, download your model and convert it to Keras (.h5) format.")

uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("\n")
    st.subheader("Prediction")
    st.text("Model prediction would appear here (fresh / leftover / spoiled).")
    st.success("Example: Fresh Food - 92% confidence")

st.markdown("---")
st.caption("Project by [Your Name / Team] · AI for Good · SDG 12")
