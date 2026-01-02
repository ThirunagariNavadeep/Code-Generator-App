# Code-Generator-App

The Code Generator App is a local AI-powered coding assistant built using Streamlit, LangChain, and Ollama (CodeLlama).
It allows users to ask programming-related questions and receive code-only responses without explanations, making it ideal for quick coding tasks, practice, and prototyping.

This application runs entirely on a local machine, ensuring privacy and offline usability while leveraging large language models.

🚀 Key Features

🔹 Code-only responses (no explanations unless explicitly requested)

🔹 Uses CodeLlama via Ollama for high-quality code generation

🔹 Clean and simple Streamlit UI

🔹 Supports local execution (no cloud dependency)

🔹 Stable integration using LangChain pipelines

🔹 Proper error handling to avoid blank screens or crashes

🛠️ Tech Stack

Python

Streamlit – for the web interface

LangChain – for prompt templating and chaining

Ollama – for running CodeLlama locally

CodeLlama – large language model optimized for code generation

📂 How It Works

The user enters a coding-related query (e.g., “reverse a string in python”).

A strict system prompt instructs the model to return only valid code.

LangChain formats the prompt and sends it to CodeLlama via Ollama.

The generated code is displayed using st.code() for better readability.

Errors (if any) are safely handled and shown in the UI.

▶️ Running the Application

Start the Ollama server:

ollama serve


Run the Streamlit app:

python -m streamlit run coding_app.py


Open the browser at:

http://localhost:8506

✅ Example Usage

Input:

write a python function to check palindrome


Output:

def is_palindrome(s):
    return s == s[::-1]

🎯 Use Cases

Coding practice

Interview preparation

Quick code generation

Offline AI coding assistant

Learning syntax without verbose explanations
