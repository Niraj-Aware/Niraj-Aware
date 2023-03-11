import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:")

# Page title
st.title("Welcome to my Streamlit app!")

# Add input fields for questions
question1 = st.text_input("Enter your first question:")
question2 = st.text_input("Enter your second question:")

# Add a submit button
if st.button("Submit"):
    # Show the submitted questions
    st.write("Question 1: " + question1)
    st.write("Question 2: " + question2)
