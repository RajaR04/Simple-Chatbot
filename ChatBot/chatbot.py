import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate.from_template(" {topic}.")

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

if __name__=="__main__":
    st.title("Basic Chatbot🤖")
    
    # Input field for user to enter topic
    topic = st.text_input("Enter Your Topic:", "")
    
    # Button to generate chain
    if st.button("Generate "):
        # Generate response using LLMChain
        res = chain.run(topic=topic)
        # Display response
        st.write("Generated Tweet:")
        st.write(res)