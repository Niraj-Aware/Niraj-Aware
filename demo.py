import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set page title and favicon
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:")

# Page title
st.title("Welcome to my Streamlit app!")

# Add input fields for questions
question1 = st.text_input("Enter your first question:")
question2 = st.text_input("Enter your second question:")

# Add a submit button
if st.button("Submit"):
    # Compare the two questions using the TF-IDF approach
    vectorizer = TfidfVectorizer()
    question1_vector = vectorizer.fit_transform([question1])
    question2_vector = vectorizer.transform([question2])
    similarity = cosine_similarity(question1_vector, question2_vector)

    # Show the accuracy score
    st.write(f"Accuracy score: {similarity[0][0]}")
