import streamlit as st
import pandas as pd

def show():
    st.title("Cohort Overview Dashboard")

    participants_df = st.session_state.participants_df
    teams_df = st.session_state.teams_df
    tasks_df = st.session_state.tasks_df
    progress_df = st.session_state.progress_df
    evaluations_df = st.session_state.evaluations_df

    st.subheader("Participants")
    st.dataframe(participants_df)

    st.subheader("Teams")
    st.dataframe(teams_df)

    st.subheader("Tasks")
    st.dataframe(tasks_df)

    st.subheader("Daily Progress")
    st.dataframe(progress_df)

    st.subheader("Evaluations")
    st.dataframe(evaluations_df)