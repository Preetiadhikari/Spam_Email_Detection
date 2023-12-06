import streamlit as st
import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string

nltk.download("punkt")


def lowerChange(text):
    return text.lower()


def transform_message(text):
    # Remove punctations & numbers
    text = re.sub(r"[^a-zA-Z]", " ", text)

    # tokenize sentence into words
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    return " ".join(words)


v = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))


# making website for checking either email is spam or not

st.title("Email Spam Detector")

input_sms = st.text_input("Enter the message")

option = st.selectbox("Message From:-", ["via Email", "other"])
if st.checkbox("check me"):
    st.write("")

if st.button("Click to Predict"):
    transform_msg = transform_message(input_sms)
    vector_input = v.transform([transform_msg])
    result = model.predict(vector_input)[0]

if result == 1:
    st.header("spam")
else:
    st.header("Ham")
