import streamlit as st
import pandas as pd
from utils.groq_llm import groq_chat_completion

def show():
    st.title("Admin Panel – Team Assignment")

    participants_df = st.session_state.participants_df
    pending_users = participants_df[participants_df["Status"] == "Approved"]

    if st.button("Generate Balanced Teams with GROQ"):
        prompt = """
        You are a team formation assistant. Based on the following approved participants' 

        Name | Role Preference | Experience | Background

        """
        for _, row in pending_users.iterrows():
            prompt += f"{row['Name']} | {row['Role Preference 1']} | {row['Experience Level']} | {row['Background']}\n"

        prompt += """
        Group them into balanced teams of 6 people. Ensure each team has a mix of roles and experience levels.
        Output format: Team Name: Member1, Member2, ...
        """

        try:
            response = groq_chat_completion(prompt)
            st.markdown("### Generated Teams:")
            st.code(response)

            lines = response.strip().split("\n")
            team_data = []
            for line in lines:
                if ":" in line:
                    team_name, members = line.split(":", 1)
                    team_data.append({"Team Name": team_name.strip(), "Members": members.strip()})

            team_df = pd.DataFrame(team_data)
            team_df.to_csv("data/teams.csv", index=False)
            st.success("Teams saved!")
        except Exception as e:
            st.error("Error generating teams. Make sure GROQ API key is valid.")

    st.subheader("Current Participants")
    st.dataframe(participants_df)

    st.subheader("Current Teams")
    st.dataframe(pd.read_csv("data/teams.csv"))