import streamlit as st
import requests
import os
import pandas as pd


TRANSCRIPTS_FOLDER = r"/workspaces/Text-Sentimental-Analysis/transcript"


st.title("Sentiment Analysis on Call Transcripts with Pretrained Models")

st.subheader("Upload Transcript Files")
uploaded_file = st.file_uploader("Upload a transcript file (.txt)", type="txt")

if uploaded_file:
    
    content = uploaded_file.read().decode("utf-8")
    st.text_area("Transcript Content", content, height=300)
    
    if st.button("Analyze Sentiment"):
        
        response = requests.post("http://127.0.0.1:5000/analyze", json={"transcript": content})
        if response.status_code == 200:
            analysis_result = response.json()
            st.subheader("Chunk Analysis Results")
            st.write(pd.DataFrame(analysis_result["chunk_results"]))
            
            st.subheader("Overall Sentiment Reasoning")
            st.write(f"*Overall Sentiment*: {analysis_result['overall_sentiment']}")
            st.write(f"*Positive Score*: {analysis_result['positive_score']}")
            st.write(f"*Negative Score*: {analysis_result['negative_score']}")
            st.write(f"*Total Score*: {analysis_result['total_score']}")
        else:
            st.error("Error analyzing sentiment.")

st.subheader("Analyze All Transcripts in Folder")
if st.button("Analyze All Transcripts"):
    if os.path.exists(TRANSCRIPTS_FOLDER):
        st.write(f"Reading transcripts from: {TRANSCRIPTS_FOLDER}")
        
       
        response = requests.get("http://127.0.0.1:5000/analyze_all")
        if response.status_code == 200:
            all_results = response.json()
            for file_name, result in all_results.items():
                st.write(f"*{file_name}:*")
                st.write(f"Overall Sentiment: {result['overall_sentiment']}")
                st.write(pd.DataFrame(result["chunk_results"]))
        else:
            st.error("Error analyzing transcripts.")
    else:
        st.error(f"Transcripts folder not found at: {TRANSCRIPTS_FOLDER}")

st.subheader("Sentiment Visualization")
if uploaded_file:
    
    st.bar_chart([1, 2, 3])  