import streamlit as st
import pandas as pd

# Configure page layout
st.set_page_config(page_title="AIEagles GenAI Cohort Signup", layout="wide")

# Load participant data
try:
    participants_df = pd.read_csv("data/participants.csv")
except FileNotFoundError:
    # Create an empty DataFrame if the file doesn't exist
    participants_df = pd.DataFrame(columns=[
        "Name", "Email", "Preferred Name", "Experience Level", "GenAI Experience",
        "Background", "Why Join?", "Goals", "Role Preference 1", "Role Preference 2",
        "Skills for Role", "Available Daily?", "Best Time to Meet", "Has Computer & Internet",
        "Comfortable with Tools", "Other Tools Known", "Additional Info", "Mentor Future Cohorts?",
        "Status"
    ])

# Title
st.title("Sign Up for the GenAI Cohort")

# Form fields
name = st.text_input("Full Name", key="name")
email = st.text_input("Email", key="email")
pref_name = st.text_input("Preferred Name", key="pref_name")
exp_level = st.selectbox(
    "Experience Level",
    ["No experience", "Beginner", "Intermediate", "Advanced"],
    key="exp_level"
)
genai_exp = st.checkbox("Have GenAI Experience?", key="genai_exp")
background = st.multiselect(
    "Background",
    ["Student", "Professional", "Hobbyist", "Educator", "Other"],
    key="background"
)
why_join = st.text_area("Why do you want to join?", key="why_join")
goals = st.text_area("What are your goals?", key="goals")
role_pref1 = st.selectbox(
    "Role Preference 1",
    ["Project Lead", "AI Explorer", "Builder", "UX Designer", "Tester", "Documenter"],
    key="role_pref1"
)
role_pref2 = st.selectbox(
    "Role Preference 2",
    ["Project Lead", "AI Explorer", "Builder", "UX Designer", "Tester", "Documenter"],
    key="role_pref2"
)
skills = st.text_area("Skills for Role", key="skills")
available = st.checkbox("Can participate daily?", key="available")
best_time = st.selectbox(
    "Best Time to Meet",
    ["Morning", "Midday", "Evening", "Flexible"],
    key="best_time"
)
has_pc = st.checkbox("Has computer & internet?", key="has_pc")
tools = st.multiselect(
    "Comfortable with Tools",
    ["Google Sheets", "GitHub", "Notion"],
    key="tools"
)
other_tools = st.text_input("Other Tools Known", key="other_tools")
additional_info = st.text_area("Anything else?", key="additional_info")
mentor_future = st.checkbox("Willing to mentor future cohorts?", key="mentor_future")

# Submit button
if st.button("Submit", key="submit"):
    new_data = pd.DataFrame([{
        "Name": name,
        "Email": email,
        "Preferred Name": pref_name,
        "Experience Level": exp_level,
        "GenAI Experience": genai_exp,
        "Background": ", ".join(background),
        "Why Join?": why_join,
        "Goals": goals,
        "Role Preference 1": role_pref1,
        "Role Preference 2": role_pref2,
        "Skills for Role": skills,
        "Available Daily?": available,
        "Best Time to Meet": best_time,
        "Has Computer & Internet": has_pc,
        "Comfortable with Tools": ", ".join(tools),
        "Other Tools Known": other_tools,
        "Additional Info": additional_info,
        "Mentor Future Cohorts?": mentor_future,
        "Status": "Pending"  # Default status for new signups
    }])
    participants_df = pd.concat([participants_df, new_data], ignore_index=True)
    participants_df.to_csv("data/participants.csv", index=False)
    st.success("Submitted successfully! Please wait for admin approval.")