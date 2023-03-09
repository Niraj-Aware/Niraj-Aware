
import streamlit as st

# Create a button and a text box
button = st.button("Click me!")
text_box = st.text_input("Enter your name")

# Display the user's input when the button is clicked
if button:
    st.write("Hello, " + text_box + "!")
