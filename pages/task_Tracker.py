import streamlit as st
import pandas as pd

def show():
    st.title("Task Tracker")

    tasks_df = st.session_state.tasks_df
    participants_df = st.session_state.participants_df

    st.subheader("Assign New Task")
    team = st.text_input("Team Name")
    task = st.text_area("Task Description")
    assign_to = st.selectbox("Assign To", participants_df["Email"].unique())
    due_date = st.date_input("Due Date")
    status = st.selectbox("Status", ["Pending", "In Progress", "Done"])

    if st.button("Add Task"):
        new_task = pd.DataFrame([{
            "Team": team,
            "Task": task,
            "Assigned To": assign_to,
            "Due Date": str(due_date),
            "Status": status
        }])
        updated_tasks = pd.concat([tasks_df, new_task], ignore_index=True)
        updated_tasks.to_csv("data/tasks.csv", index=False)
        st.success("Task added!")

    st.subheader("Current Tasks")
    st.dataframe(tasks_df)