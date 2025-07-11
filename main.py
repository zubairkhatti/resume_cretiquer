
import streamlit as st
import PyPDF2
import io
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

upload_resume = st.file_uploader("Upload your Resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")
analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(upload_resume):
    if upload_resume.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(upload_resume.read()))
    return upload_resume.read().decode("utf-8")

if analyze_button and upload_resume:
    try:
        file_content = extract_text_from_file(upload_resume)
        if not file_content.strip():
            st.error("File does not have any content!")
            st.stop()
        
        # Create chat prompt
        system_msg = SystemMessage(
            content="You are an expert resume reviewer with years of experience in HR and recruitment."
        )
        user_prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        
        Resume content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specific recommendations."""
        
        user_msg = HumanMessage(content=user_prompt)

        # Gemini Model
        client = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.7,
            google_api_key=GOOGLE_API_KEY
        )

        response = client.invoke([system_msg, user_msg])

        st.markdown("### Analysis Results")
        st.markdown(response.content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
