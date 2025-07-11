import streamlit as st
import pandas as pd

def show():
    st.title("Sign Up for the Cohort")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    role = st.selectbox("Preferred Role", ["Project Lead", "AI Explorer", "Builder", "UX Designer", "Tester", "Documenter"])
    experience = st.selectbox("Experience Level", ["No experience", "Beginner", "Intermediate", "Advanced"])
    interest = st.text_input("Area of Interest")

    if st.button("Submit"):
        new_data = pd.DataFrame([{
            "Name": name,
            "Email": email,
            "Role": role,
            "Experience": experience,
            "Area_of_Interest": interest,
            "Status": "Pending",
            "Team": ""
        }])
        df = pd.read_csv("data/Participants.csv")
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv("data/Participants.csv", index=False)
        st.success("Submitted successfully!")