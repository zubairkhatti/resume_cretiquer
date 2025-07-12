# AI Resume Critiquer

**Overview:**
AI Resume Critiquer is a web-based application that allows users to upload their resume (PDF or TXT) and receive AI-powered feedback. The feedback is generated using Google's Gemini model (gemini-1.5-flash) integrated with LangChain.

**Technologies Used:**
- Streamlit for web interface
- PyPDF2 and io for reading PDF contents
- dotenv and os for secure API key loading
- LangChain for prompt structuring and messaging
- Gemini (via ChatGoogleGenerativeAI) for LLM-based feedback

**Flow:**
1. User uploads a resume and optionally enters a target job role.
2. PDF or TXT file is parsed into plain text.
3. A structured prompt is created with user content and instructions.
4. Prompt is sent to Gemini model which returns the analysis.
5. Feedback is displayed in the Streamlit UI.

**Purpose:**
To help users improve their resumes by giving content-specific suggestions based on AI analysis.