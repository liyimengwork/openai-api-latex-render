import streamlit as st
import re

# Function to replace LaTeX delimiters
def replace_latex_delimiters(text):
    # Replace inline math delimiters \(...\) with \[...\]
    text = re.sub(r'\\\((.*?)\\\)', r'\\[\1\\]', text, flags=re.DOTALL)
    # Replace inline math delimiters \(...\) with $...$
    text = re.sub(r'\\\((.*?)\\\)', r'$\1$', text, flags=re.DOTALL)
    return text

# Create a text input area for user to enter text
input_text = st.text_area("Paste OpenAI-API-generated content with LaTeX expressions here:", height=400)

# If the user provides input, process and display it
if input_text:
    # Process the input text to replace LaTeX delimiters
    processed_text = replace_latex_delimiters(input_text)

    # Display the processed text with LaTeX rendered
    st.markdown(processed_text)
