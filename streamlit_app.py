import streamlit as st
import os
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
st.markdown("""
          <style>
          footer {visibility: hidden;}
          </style>""", unsafe_allow_html=True)

with st.sidebar:
        
        os.environ['OPENAI_API_KEY'] = st.text_input('Your OpenAI API KEY', type="password")


# Title
st.title('Greenlync Guru')

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Create CSV Agent
    agent = create_csv_agent(OpenAI(temperature=0), uploaded_file, verbose=True)

    # Ask a question
    question = st.text_input('Ask a question about the data')

    if question:
        # Run the agent with the question
        st.write(agent.run(question))
