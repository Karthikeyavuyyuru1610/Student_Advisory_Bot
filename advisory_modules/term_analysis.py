# advisory_modules/term_analysis.py

import pandas as pd

def analyze_academic_strengths(emplid, term_df):
    student_terms = term_df[term_df["EMPLID"] == emplid]

    if student_terms.empty:
        return {"summary": "No term data available.", "strengths": []}

    # Convert and filter
    student_terms["TERM_GPA"] = pd.to_numeric(student_terms["TERM_GPA"], errors="coerce")
    valid_gpas = student_terms.dropna(subset=["TERM_GPA"])

    if valid_gpas.empty:
        return {"summary": "No valid GPA records found.", "strengths": ["Needs Improvement"]}

    avg_gpa = valid_gpas["TERM_GPA"].mean()
    strengths = []

    if avg_gpa >= 3.5:
        strengths.append("High GPA - Honors Level")
    elif avg_gpa >= 3.0:
        strengths.append("Above Average GPA")
    elif avg_gpa >= 2.0:
        strengths.append("Average GPA")
    else:
        strengths.append("Needs Improvement")

    return {
        "average_gpa": round(avg_gpa, 2),
        "summary": f"Average GPA: {round(avg_gpa, 2)}",
        "strengths": strengths
    }
