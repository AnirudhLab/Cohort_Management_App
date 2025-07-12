import streamlit as st
import pandas as pd
import toml

# Page config
st.set_page_config(page_title="GenAI Cohort", layout="wide")

# Load data
participants_df = pd.read_csv("data/participants.csv")
teams_df = pd.read_csv("data/teams.csv")
tasks_df = pd.read_csv("data/tasks.csv")
progress_df = pd.read_csv("data/daily_progress.csv")
evaluations_df = pd.read_csv("data/evaluations.csv")

# Store in session state
st.session_state.participants_df = participants_df
st.session_state.teams_df = teams_df
st.session_state.tasks_df = tasks_df
st.session_state.progress_df = progress_df
st.session_state.evaluations_df = evaluations_df

# Login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_email = None

st.sidebar.title("GenAI Cohort App")

# Logout
if st.session_state.logged_in and st.sidebar.button("Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# ✅ Login + Signup Section (for non-logged-in users)
if not st.session_state.logged_in:
    st.sidebar.subheader("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        secrets = toml.load(".streamlit/secrets.toml")
        if email in secrets["ADMIN_EMAILS"] and password == secrets["ADMIN_PASSWORD"]:
            st.session_state.logged_in = True
            st.session_state.user_role = "admin"
            st.session_state.user_email = email
            st.rerun()
        elif email in participants_df["Email"].values:
            status = participants_df[participants_df["Email"] == email]["Status"].iloc[0]
            if status == "Approved":
                st.session_state.logged_in = True
                st.session_state.user_role = "participant"
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Your account is still pending approval.")
        else:
            st.error("Invalid credentials.")

    # ✅ Show signup form before login — on main page
    from modules import signup
    signup.show()
    st.stop()

# ✅ Navigation and Pages (post login)
st.sidebar.subheader("Navigation")
if st.session_state.user_role == "admin":
    page = st.sidebar.selectbox("Go to", ["AI Team Matching"])
else:
    page = st.sidebar.selectbox("Go to", ["Daily Progress"])

from modules import ai_team_matching, daily_progress

if page == "AI Team Matching":
    ai_team_matching.show()
elif page == "Daily Progress":
    daily_progress.show()
