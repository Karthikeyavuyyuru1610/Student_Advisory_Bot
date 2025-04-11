# advisory_modules/elective_recommendation.py

def recommend_electives(acad_prog, strengths, enrollment_df):
    # Ensure ACAD_PROG is string
    acad_prog = str(acad_prog) if acad_prog is not None else ""
    enrollment_df["ACAD_PROG"] = enrollment_df["ACAD_PROG"].astype(str)

    # Fallback if program is missing
    if not acad_prog.strip() or acad_prog.strip().lower() == "nan":
        print("⚠️ ACAD_PROG is missing or NaN. Assigning fallback program 'GENERIC'")
        acad_prog = "GENERIC"

    # Sample elective pools by program
    program_electives = {
        "ICECS": [
            "Introduction to Programming",
            "Signals and Systems",
            "Network Security",
            "Embedded Systems",
            "Renewable Energy Systems"
        ],
        "ICOBA": [
            "Business Analytics",
            "Marketing Strategy",
            "Digital Transformation",
            "Entrepreneurship"
        ],
        "GENERIC": [
            "Creative Thinking",
            "Communication Skills",
            "Fundamentals of Research",
            "Introduction to Problem Solving"
        ]
    }

    # Try to find student and what they've already taken
    matching = enrollment_df[
        enrollment_df["ACAD_PROG"].str.upper().str.strip() == acad_prog.upper().strip()
    ]
    
    if matching.empty:
        print(f"⚠️ No matching student found for ACAD_PROG: {acad_prog}. Assuming no electives taken.")
        taken_courses = []
    else:
        student_row = matching.iloc[0]
        taken_courses = [c.lower() for c in student_row.get("COURSES_TAKEN", []) if isinstance(c, str)]

    # Recommend electives not yet taken
    electives = program_electives.get(acad_prog.upper(), program_electives["GENERIC"])
    recommended = [e for e in electives if e.lower() not in taken_courses]

    return recommended
