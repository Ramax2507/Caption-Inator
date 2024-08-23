import requests
import streamlit as st

# Streamlit title
st.title("Caption-Inator!!!")

# Hugging Face API endpoint and authentication
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

# Function to query the model
def query(file):
    data = file.read()  # Read the file data
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# File uploader in Streamlit
uploaded_file = st.file_uploader("Upload your image", type="jpg")

# If a file is uploaded
if uploaded_file is not None:
    # Query the model with the uploaded image
    st.image(uploaded_file )
    output = query(uploaded_file)

    # Extract the caption text
    caption = output[0]["generated_text"]

    # Display the caption
    st.write( caption)
