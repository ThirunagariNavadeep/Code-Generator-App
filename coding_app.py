import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM



st.set_page_config(
    page_title="Code Generator App",
    layout="centered"
)

st.title("Code Generator App")

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a expert coding assistant. "
            "Return ONLY valid code. "
            "Do NOT explain anything. "
            "Do NOT add markdown. "
            "Do NOT add comments unless explicitly asked."
        ),
        ("user", "{question}")
    ]
)

input_text = st.text_input("Ask a coding question")


llm = OllamaLLM(model="codellama")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        response = chain.invoke({"question": input_text})
        st.code(response)  # shows clean code output
    except Exception as e:
        st.error("Error while generating code")
        st.exception(e)




