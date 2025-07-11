import streamlit as st
import pandas as pd

st.set_page_config(page_title="GenAI Cohort", layout="centered")

# Load participants
participants_df = pd.read_csv("data/Participants.csv")
st.session_state.participants_df = participants_df

# Simple auth
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = "participant"

# Login
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Check if user is admin
    if email in st.secrets.ADMIN_EMAILS and password == st.secrets.ADMIN_PASSWORD:
        st.session_state.logged_in = True
        st.session_state.user_role = "admin"
        st.success(f"Logged in as Admin ({email})")
    
    # Check if user is participant and approved
    elif email in participants_df["Email"].values:
        user_status = participants_df[participants_df["Email"] == email]["Status"].iloc[0]
        if user_status == "Approved":
            st.session_state.logged_in = True
            st.session_state.user_role = "participant"
            st.session_state.user_email = email
            st.success("Logged in as Participant")
        else:
            st.error("Your account is still pending approval.")
    else:
        st.error("Invalid credentials.")

if st.session_state.logged_in:
    st.sidebar.title("Navigation")
    if st.session_state.user_role == "admin":
        page = st.sidebar.selectbox("Go to", ["Signup", "AI Team Matching", "Daily Summary"])
    else:
        page = st.sidebar.selectbox("Go to", ["Daily Summary"])

    if page == "Signup":
        from pages import signup as signup_page
        signup_page.show()
    elif page == "AI Team Matching":
        from pages import ai_team_matching as ai_team_page
        ai_team_page.show()
    elif page == "Daily Summary":
        from pages import daily_summary as daily_summary_page
        daily_summary_page.show()