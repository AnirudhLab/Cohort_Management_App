import streamlit as st
import pandas as pd

def show():
    st.title("Sign Up for the Cohort")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    pref_name = st.text_input("Preferred Name")
    exp_level = st.selectbox("Experience Level", ["No experience", "Beginner", "Intermediate", "Advanced"])
    genai_exp = st.checkbox("Have GenAI Experience?")
    background = st.multiselect("Background", ["Student", "Professional", "Hobbyist", "Educator", "Other"])
    why_join = st.text_area("Why do you want to join?")
    goals = st.text_area("What are your goals?")
    role_pref1 = st.selectbox("Role Preference 1", ["Project Lead", "AI Explorer", "Builder", "UX Designer", "Tester", "Documenter"])
    role_pref2 = st.selectbox("Role Preference 2", ["Project Lead", "AI Explorer", "Builder", "UX Designer", "Tester", "Documenter"])
    skills = st.text_area("Skills for Role")
    available = st.checkbox("Can participate daily?")
    best_time = st.selectbox("Best Time to Meet", ["Morning", "Midday", "Evening", "Flexible"])
    has_pc = st.checkbox("Has computer & internet?")
    tools = st.multiselect("Comfortable with Tools", ["Google Docs", "GitHub", "Notion"])
    other_tools = st.text_input("Other Tools Known")
    additional_info = st.text_area("Anything else?")
    mentor_future = st.checkbox("Willing to mentor future cohorts?")

    if st.button("Submit"):
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
            "Status": "Pending"
        }])
        df = pd.read_csv("data/participants.csv")
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv("data/participants.csv", index=False)
        st.success("Submitted successfully!")