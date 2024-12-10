import os
import zipfile
import shutil
import tempfile
import time
import logging
from groq import Groq
import streamlit as st

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Initialize the Groq client
api_key = "API_KEY"  # Replace with your Groq API key
client = Groq(api_key=api_key)

# Function to analyze code with Groq, with enhanced backoff
def analyze_code_with_groq(file_path, retries=5):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        file_content = f.read()

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[ 
                {"role": "system", "content": "You are an expert code reviewer."},
                {"role": "user", "content": f"Analyze the following code and provide detailed documentation in a professional format:\n\n{file_content}"}
            ],
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            stream=False,
        )
        
        if hasattr(completion.choices[0].message, 'content'):
            return completion.choices[0].message.content
        else:
            return "Error: Unexpected response structure."

    except Exception as e:
        logging.error(f"Error analyzing file {file_path}: {str(e)}")  # Log the error
        if "Rate limit reached" in str(e) and retries > 0:
            # Exponential backoff: wait 2, 4, 8, etc. seconds
            wait_time = 2 ** (5 - retries)  # Increase wait time between retries
            st.warning(f"Rate limit reached, retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            return analyze_code_with_groq(file_path, retries - 1)  # Retry after waiting

        return f"Error analyzing file {file_path}: {e}"

# Function to handle file extraction from zip
def process_uploaded_zip(uploaded_file):
    temp_dir = tempfile.mkdtemp()  # Temporary directory
    try:
        zip_path = os.path.join(temp_dir, "uploaded_project.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        return temp_dir
    except Exception as e:
        shutil.rmtree(temp_dir)
        st.error(f"Error processing zip file: {e}")
        return None

# Function to analyze all files in a folder recursively
def analyze_project_folder(folder_path):
    documentation = []
    for root, dirs, files in os.walk(folder_path):  # Walk through all files in all subfolders
        for file in files:
            file_path = os.path.join(root, file)
            doc = analyze_code_with_groq(file_path)
            documentation.append((file_path, doc))
    return documentation

# Function to format documentation
def format_documentation(file_path, doc_content):
    if "Error analyzing" in doc_content:
        doc_content = f"**Error**: Could not analyze this file due to rate limiting or other issues."
    return f"""
# Documentation for {file_path}

## Description
The file is analyzed to extract key information and provide a detailed explanation of its functionality.

## Code Overview
{doc_content}

## Key Functions and Classes
- [Function/Class Name]: Brief description of purpose and functionality.

## Dependencies (if applicable)
List any dependencies or external libraries used within the file.

## Usage
Provide example usages or instructions for using any code components in the file.

## Notes
Any additional notes, such as limitations, edge cases, or special considerations.
"""

# Streamlit UI
st.set_page_config(page_title="AI Code Documentation Generator", page_icon=":memo:", layout="wide")
st.title("AI Code Documentation Generator")
st.write("""
Upload a zip file containing your project to generate documentation automatically. The documentation will describe the code and provide insights into its functionality.
""")

# File uploader (accept zip files only)
uploaded_file = st.file_uploader("Upload a zip file", type="zip")

if uploaded_file and st.button("Analyze"):
    temp_dir = None
    if uploaded_file:
        st.info("Processing uploaded zip file...")
        temp_dir = process_uploaded_zip(uploaded_file)
        if not temp_dir:
            st.error("Failed to process zip file.")
            st.stop()

    st.info("Analyzing files...")
    documentation = analyze_project_folder(temp_dir)

    st.header("Generated Documentation")

    # Display documentation for each file in the uploaded zip
    for file_path, doc in documentation:
        st.subheader(f"Documentation for: {file_path}")
        st.markdown(doc)  # Display the generated documentation in markdown format

    # Allow user to download documentation
    if documentation:
        st.info("Click below to download the generated documentation as a markdown file.")
        doc_file = os.path.join(temp_dir, "documentation.md")
        with open(doc_file, "w", encoding="utf-8") as f:
            for file_path, doc in documentation:
                formatted_doc = format_documentation(file_path, doc)
                f.write(formatted_doc)

        with open(doc_file, "rb") as f:
            st.download_button(
                label="Download Documentation as Markdown",
                data=f,
                file_name="documentation.md",
                mime="text/markdown"
            )

    if uploaded_file and temp_dir:
        shutil.rmtree(temp_dir)  # Clean up the temporary directory
