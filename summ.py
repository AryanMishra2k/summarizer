from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

import streamlit as st

st.title('Summarizer')
ARTICLE = st.text_area('Enter your text:')

if st.button('Generate Summary'):
    summary = summarizer(ARTICLE, max_length=400, min_length=100, do_sample=False)
    st.write('Summary of the Text:')
    st.write(summary)

