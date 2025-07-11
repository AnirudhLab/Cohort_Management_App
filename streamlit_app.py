import streamlit as st
import pandas as pd

st.set_page_config(page_title="GenAI Cohort", layout="wide")

# Load all data
participants_df = pd.read_csv("data/participants.csv")
teams_df = pd.read_csv("data/teams.csv")
tasks_df = pd.read_csv("data/tasks.csv")
progress_df = pd.read_csv("data/daily_progress.csv")
evaluations_df = pd.read_csv("data/evaluations.csv")

st.session_state.participants_df = participants_df
st.session_state.teams_df = teams_df
st.session_state.tasks_df = tasks_df
st.session_state.progress_df = progress_df
st.session_state.evaluations_df = evaluations_df

# Simple auth
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = "participant"

# Login
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email in st.secrets.ADMIN_EMAILS and password == st.secrets.ADMIN_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.user_role = "admin"
        st.success(f"Logged in as Admin ({email})")

    elif email in participants_df["Email"].values:
        user_status = participants_df[participants_df["Email"] == email]["Status"].iloc[0]
        if user_status == "Approved":
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.user_role = "participant"
            st.success("Logged in as Participant")
        else:
            st.error("Your account is still pending approval.")
    else:
        st.error("Invalid credentials.")

if st.session_state.logged_in:
    st.sidebar.title("Navigation")
    if st.session_state.user_role == "admin":
        page = st.sidebar.selectbox("Go to", [
            "Signup",
            "Admin Panel",
            "Task Tracker",
            "Daily Progress",
            "Cohort Overview"
        ])
    else:
        page = st.sidebar.selectbox("Go to", [
            "Daily Progress",
            "Cohort Overview"
        ])

    if page == "Signup":
        from pages import signup
        signup.show()
    elif page == "Admin Panel":
        from pages import admin_Panel
        admin_Panel.show()
    elif page == "Task Tracker":
        from pages import task_Tracker
        task_Tracker.show()
    elif page == "Daily Progress":
        from pages import daily_progress
        daily_progress.show()
    elif page == "Cohort Overview":
        from pages import cohort_overview
        cohort_overview.show()