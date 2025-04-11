# advisory_modules/response_generator.py

import google.generativeai as genai

# 🔐 Directly use your API key here
API_KEY = "PLACE_API_KEY"  # Here i am removing my api key to run this project place a api key from google cloud console
MODEL = "models/gemini-2.0-flash"  

genai.configure(api_key=API_KEY)

def response_generator(user_prompt, student_info, available_electives, strengths):
    # Format electives
    elective_details = ""
    for elective in available_electives:
        schedules = "\n    ".join([
            f"Term: {s.get('Term', 'N/A')}, Days: {s.get('Days', 'N/A')}, Time: {s.get('Mtg Start', 'N/A')} - {s.get('Mtg End', 'N/A')}, Instructor: {s.get('Instructor', 'N/A')}"
            for s in elective.get('schedule', [])
        ])
        elective_details += f"- {elective.get('course', 'Unnamed Course')}\n    {schedules}\n\n"

    if not elective_details.strip():
        fallback = ["Business Analytics", "Entrepreneurship", "Innovation Lab", "Operations Management", "Communication Skills"]
        elective_details = "Suggested electives:\n" + "\n".join(f"- {e}" for e in fallback)

    # Academic context
    context = f"""
Student Name: {student_info['NAME']}
Student ID: {student_info['EMPLID']}
Academic Program: {student_info.get('ACAD_PROG', 'N/A')}
Program Status: {student_info.get('PROG_STATUS', 'N/A')}

GPA Summary: {strengths.get('summary', 'N/A')}
Strength Tags: {', '.join(strengths.get('strengths', []))}

Available Electives:
{elective_details}
"""

    final_prompt = f"""You are an intelligent academic advisor bot. The student has asked:

\"{user_prompt}\"

Based on the academic context below, provide:
1. A summary of the student's academic profile.
2. An analysis of their strengths and academic performance.
3. Elective course suggestions that align with their program and strengths.
4. A final academic advisory message.

Academic Context:
{context}
"""

    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(final_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
