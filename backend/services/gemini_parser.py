import json
import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def parse_resume_with_gemini(resume_text):

    prompt = f"""
You are an expert ATS Resume Parser.

Extract the following information.

Return ONLY valid JSON.

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "education":[],
    "projects":[],
    "experience":[],
    "certifications":[]
}}

Resume:

{resume_text}

"""

    response = model.generate_content(prompt)

    cleaned = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned)