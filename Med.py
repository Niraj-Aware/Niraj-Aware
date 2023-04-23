import streamlit as st
import cv2
import pytesseract
from PIL import Image

# Configure pytesseract to use English language
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata" -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,-'

# Define the Streamlit app
def app():
    st.title("Medicine Prescription Detection")

    # Get user input
    uploaded_file = st.file_uploader("Upload a medicine prescription image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Convert the image to grayscale
        gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(gray, lang='eng', config=tessdata_dir_config)

        # Extract the names of the medicines from the text
        meds = []
        for line in text.split('\n'):
            line = line.strip()
            if any(word in line.lower() for word in ['tablet', 'capsule', 'injection', 'syrup', 'ointment']):
                words = line.split()
                for i, word in enumerate(words):
                    if word.lower() in ['tablet', 'capsule', 'injection', 'syrup', 'ointment']:
                        med = ' '.join(words[i+1:])
                        meds.append(med)
                        break

        if len(meds) > 0:
            st.write("Medicines:")
            for med in meds:
                st.write(med)
        else:
            st.write("No medicines found in prescription.")

