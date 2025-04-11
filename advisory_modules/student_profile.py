# advisory_modules/student_profile.py

def get_student_profile(student_name, enrollment_df, program_df):
    student_row = enrollment_df[enrollment_df["NAME"].str.contains(student_name, case=False, na=False)]
    
    if student_row.empty:
        raise ValueError(f"Student '{student_name}' not found.")

    emplid = student_row["EMPLID"].iloc[0]
    acad_prog = student_row["ACAD_PROG"].iloc[0]

    program_row = program_df[program_df["EMPLID"] == emplid]
    program_status = program_row["PROG_STATUS"].iloc[0] if not program_row.empty else "Unknown"

    return {
        "NAME": student_row["NAME"].iloc[0],
        "EMPLID": emplid,
        "ACAD_PROG": acad_prog,
        "PROG_STATUS": program_status,
        "COURSES": student_row["COURSES_TAKEN"].iloc[0] if "COURSES_TAKEN" in student_row else []
    }
