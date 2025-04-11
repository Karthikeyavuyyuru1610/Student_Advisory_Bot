import streamlit as st
import pandas as pd
from advisory_modules.student_profile import get_student_profile
from advisory_modules.term_analysis import analyze_academic_strengths
from advisory_modules.Schdule_checker import check_schedule_availability
from advisory_modules.response_generator import response_generator
from advisory_modules.elective_recommendation import recommend_electives
import re

#  Load cleaned data paths
ENRICHED_STUDENT_PATH = r"C:\\Users\\mouni\\Downloads\\student_advisory_bot (1)\\data\\ENRICHED_STUDENT_PROFILE.xlsx"
CLEANED_PROG_PATH = r"C:\\Users\\mouni\\Downloads\\student_advisory_bot (1)\\data\\CLEANED_ACAD_PROG.xlsx"
CLEANED_SCHEDULE_PATH = r"C:\\Users\\mouni\\Downloads\\student_advisory_bot (1)\\data\\CLEANED_ELECTIVE_SCHEDULE.xlsx"
TERM_HISTORY_PATH = r"C:\\Users\\mouni\\Downloads\\student_advisory_bot (1)\\data\\TERM_HISTORY.xlsx"

@st.cache_data
def load_data():
    enrollment_df = pd.read_excel(ENRICHED_STUDENT_PATH)
    program_df = pd.read_excel(CLEANED_PROG_PATH)
    schedule_df = pd.read_excel(CLEANED_SCHEDULE_PATH)
    term_df = pd.read_excel(TERM_HISTORY_PATH)
    return enrollment_df, program_df, schedule_df, term_df

def extract_name_from_prompt(prompt, enrollment_df):
    for name in enrollment_df['NAME']:
        if name.lower() in prompt.lower():
            return name
    raise ValueError("No matching student name found in the prompt. Please enter the correct name. \n If your name is correct that mean we Dont have your day in our Data base. \n So now i cannot Recomment you new elective ")

# Streamlit UI setup
st.set_page_config(page_title="Student Advisory BOT", page_icon="🎓")
st.title("🎓 AI-Powered Student Advisory BOT - Middle East University")
st.write("Ask your academic advisor a question like:\n'I am Ali Abdulla Aldhaheri. Can you suggest electives that align with my major and strengths?'")

# User input box and send button
with st.form("query_form"):
    prompt_text = st.text_area("Type your question below:")
    submitted = st.form_submit_button("Send")

if submitted and prompt_text:
    with st.spinner("Analyzing your academic profile and generating recommendations..."):
        try:
            # Load data
            enrollment_df, program_df, schedule_df, term_df = load_data()

            # Extract name
            student_name = extract_name_from_prompt(prompt_text, enrollment_df)

            # Get profile
            student_info = get_student_profile(student_name, enrollment_df, program_df)

            # Analyze strengths
            strengths = analyze_academic_strengths(student_info['EMPLID'], term_df)

            # Recommend electives
            electives = recommend_electives(student_info['ACAD_PROG'], strengths, enrollment_df)

            # Match electives to schedule
            available_electives = check_schedule_availability(electives, schedule_df)

            # Fallback if no elective matched schedule
            if not available_electives:
                st.warning("No matched electives were found in the schedule. Using fallback electives for your program.")

                # Use actual courses from schedule as fallback
                fallback_schedule_df = schedule_df.dropna(subset=["COURSE_NAME"]).drop_duplicates("COURSE_NAME")
                fallback_courses = fallback_schedule_df.head(5)

                available_electives = [
                    {
                        "course": row["COURSE_NAME"],
                        "schedule": [{
                            "Term": row.get("Term", ""),
                            "Days": row.get("Days", ""),
                            "Mtg Start": row.get("Mtg Start", ""),
                            "Mtg End": row.get("Mtg End", ""),
                            "Instructor": row.get("Instructor", "")
                        }]
                    }
                    for _, row in fallback_courses.iterrows()
                ]

            # Generate LLM response
            advisory_response = response_generator(prompt_text, student_info, available_electives, strengths)

            # Display result
            st.success("Here is your personalized academic advisory response:")
            st.write(advisory_response)

        except ValueError as ve:
            st.error(f"Value Error: {ve}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            st.exception(e)