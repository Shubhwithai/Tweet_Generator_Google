import streamlit as st
import os
from google import genai

# Load Google API Key
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

client = genai.Client()

model = 'gemini-2.5-flash'

# Prompt template
tweet_template = "Give me {number} tweets on {topic}"

st.header("Tweet Generator - SATVIK")
st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")
number = st.number_input(
    "Number of tweets",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

if st.button("Generate"):
    prompt = tweet_template.format(number=number, topic=topic)

    response = client.models.generate_content(
        model=model, contents=prompt
    )

    st.write(response.text)