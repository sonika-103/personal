from dotenv import load_dotenv
load_dotenv()  # Load environment variables before using os.getenv
import streamlit as st
import os
import google.generativeai as genai

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    st.header("Chat_bot")

    input_text = st.text_input("Input: ", key="input")
    submit = st.button("Ask the question")
    if submit:
            try:
                response = get_gemini_response(input_text)
                st.subheader("The Response is")
                st.write(response)
            except Exception as e:  # Catch any errors from the API call
                st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

