import streamlit as st
import pandas as pd
from utils.groq_llm import groq_chat_completion

def show():
    st.title("AI-Based Team Matching")

    df = pd.read_csv("data/Participants.csv")
    pending_users = df[df["Status"] == "Approved"]

    if st.button("Generate Balanced Teams"):
        prompt = """
        You are a team formation assistant. Based on the following approved participants' 

        Name | Role Preference | Experience | Area of Interest

        """
        for _, row in pending_users.iterrows():
            prompt += f"{row['Name']} | {row['Role']} | {row['Experience']} | {row['Area_of_Interest']}\n"

        prompt += """
        Group them into balanced teams of 6 people. Ensure each team has a mix of roles and experience levels.
        Output format: Team Name: Member1, Member2, ...
        """

        response = groq_chat_completion(prompt)
        st.markdown("### Generated Teams:")
        st.code(response)

        # Save to CSV
        lines = response.strip().split("\n")
        team_data = []
        for line in lines:
            if ":" in line:
                team_name, members = line.split(":", 1)
                team_data.append({"Team Name": team_name.strip(), "Members": members.strip()})

        team_df = pd.DataFrame(team_data)
        team_df.to_csv("data/Teams.csv", index=False)
        st.success("Teams saved!")