import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from fuzzywuzzy import fuzz

# Load the training data
train_data = pd.read_csv('C:/Users/niraj/Downloads/train.csv')

# Define the vectorizer for the TF-IDF approach
vectorizer = TfidfVectorizer()

# Train a random forest classifier on the training data for the TF-IDF approach
X_tfidf = vectorizer.fit_transform(train_data['question1'] + ' ' + train_data['question2'])
y_tfidf = train_data['is_duplicate']
rf_tfidf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_tfidf.fit(X_tfidf, y_tfidf)


# Define the function to calculate similarity for the fuzzywuzzy approach
def similarity(question1, question2):
    return fuzz.token_sort_ratio(question1, question2)


# Calculate the similarity between the question pairs for the fuzzywuzzy approach
train_data['similarity'] = train_data.apply(lambda x: similarity(x['question1'], x['question2']), axis=1)

# Train a random forest classifier on the training data for the fuzzywuzzy approach
X_fuzzy = train_data['similarity'].values.reshape(-1, 1)
y_fuzzy = train_data['is_duplicate']
rf_fuzzy = RandomForestClassifier(n_estimators=100, random_state=42)
rf_fuzzy.fit(X_fuzzy, y_fuzzy)


# Define the Streamlit app
def app():
    st.title('Question Duplicate Detection')
    st.write('This app predicts whether two questions are duplicates or not, using two different approaches.')

    # Get user input for the first question
    q1 = st.text_input('Enter the first question:')

    # Get user input for the second question
    q2 = st.text_input('Enter the second question:')

    # Predict using the TF-IDF approach
    X_new_tfidf = vectorizer.transform([q1 + ' ' + q2])
    y_pred_tfidf = rf_tfidf.predict(X_new_tfidf)[0]
    st.write('TF-IDF approach prediction:', y_pred_tfidf)

    # Predict using the fuzzywuzzy approach
    similarity_score = similarity(q1, q2)
    y_pred_fuzzy = rf_fuzzy.predict([[similarity_score]])[0]
    st.write('Fuzzywuzzy approach prediction:', y_pred_fuzzy)

    # Display the accuracy of each approach
    st.write('TF-IDF approach accuracy:', accuracy_score(y_tfidf, rf_tfidf.predict(X_tfidf)))
    st.write('Fuzzywuzzy approach accuracy:', accuracy_score(y_fuzzy, rf_fuzzy.predict(X_fuzzy)))

