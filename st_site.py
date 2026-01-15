#ALWAYS RUN APP THRU streamlit run [name].py

import streamlit as st
from roboflow import Roboflow
from configs import RF_API_KEY, RF_WORKSPACE, RF_PROJECT, RF_VERSION
from PIL import Image
import tempfile
import os

st.title("🅿️ Parking Lot Detection")
st.write("Upload an image to detect parking spaces using AI")

# Initialize Roboflow model
@st.cache_resource
def load_model():
    rf = Roboflow(api_key=RF_API_KEY)
    project = rf.workspace(RF_WORKSPACE).project(RF_PROJECT)
    model = project.version(RF_VERSION).model
    return model

# Load the model
model = load_model()

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=True)
    
    # Save uploaded file temporarily and run detection
    if st.button("Run Detection"):
        with st.spinner("Processing image..."):
            # Save the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                tmp_file.write(uploaded_file.getbuffer())
                tmp_path = tmp_file.name
            
            try:
                # Run inference
                result = model.predict(tmp_path, confidence=40)
                
                # Save the result
                output_path = "detection_output.jpg"
                result.save(output_path)
                
                # Display the result
                result_image = Image.open(output_path)
                st.image(result_image, caption="Detection Result", width=True)
                
                # Show detection stats
                st.success("✅ Detection completed!")
                st.info(f"Predictions: {len(result.json()['predictions'])} objects detected")
                
            except Exception as e:
                st.error(f"Error during detection: {str(e)}")
            finally:
                # Clean up temporary file
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)

# Info section
with st.expander("ℹ️ About this app"):
    st.write("""
    This app uses a Roboflow AI model to detect parking spaces in images.
    - Upload a parking lot image
    - Click "Run Detection" to analyze it
    - The model will identify and highlight parking spaces
    """)