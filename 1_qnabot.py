#loading the environmental file
from dotenv import load_dotenv
load_dotenv()

#Create a ChatGroq object and invoke it
from langchain_groq import ChatGroq
llm=ChatGroq(model="openai/gpt-oss-120b")

import streamlit as st
st.title("IntelliChat")
st.markdown("It assists me in learning GenAI")
