import openai
import streamlit as st
from pathlib import Path
import configparser


cfg_reader = configparser.ConfigParser()
fpath = Path.cwd() / Path('config.ini')
cfg_reader.read(str(fpath))
openai.api_key = st.secrets['OPENAI_API_KEY']

def get_response_from_chatgpt(text):
    prompt= "Identify and return the sentiment either positive or negative in given text. text: {}".format(text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Text Sentiment Analyzer That returns concise Sentiment."},
            {"role": "user", "content": prompt }
        ],
        temperature = 0.1
    )
    sentiment = response['choices'][0]['message']['content']
    return sentiment

st.title("ChatGPT Text Sentiment Analyzer")
model="gpt-3.5-turbo"
openai_api_key = st.text_input("OpenAI API Key", key=openapi_key , type="password")
text = st.text_input("Enter Text: ", value= "I love to read AI Books")

if st.button('Submit'):
    with st.spinner('OpenAI Processing in progress'):
        sentiment = get_response_from_chatgpt(text)
        st.success('OpenAI Processing Complete')

    st.write("Sentiment: {}".format(sentiment))
