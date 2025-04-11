# advisory_modules/schedule_checker.py

def check_schedule_availability(elective_list, schedule_df):
    available = []

    # Clean and normalize schedule data
    schedule_df = schedule_df.copy()
    schedule_df["COURSE_NAME"] = schedule_df["COURSE_NAME"].fillna("").str.lower().str.strip()

    for course in elective_list:
        course_lower = course.lower().strip()
        keywords = course_lower.split()

        # Match all words in the elective title against schedule course name
        match = schedule_df[
            schedule_df["COURSE_NAME"].apply(lambda x: all(kw in x for kw in keywords))
        ]

        if not match.empty:
            print(f"✅ Match found for: {course}")
            available.append({
                "course": course,
                "schedule": match[["Term", "Days", "Mtg Start", "Mtg End", "Instructor"]].to_dict(orient="records")
            })
        else:
            print(f"❌ No match found for: {course}")

    # Optional: Log fallback options for debugging
    if not available:
        print("⚠️ No electives matched schedule. You might want to display top generic electives.")
        print("📘 Example fallback:", schedule_df["COURSE_NAME"].dropna().unique()[:3])

    return available
