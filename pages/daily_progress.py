import streamlit as st
import pandas as pd
from utils.groq_llm import groq_chat_completion

def show():
    st.title("Daily Progress Log")

    today = st.date_input("Select Date")
    team = st.text_input("Your Team Name")
    participant = st.text_input("Your Email")
    update = st.text_area("What did you work on today?")
    challenges = st.text_area("Challenges faced")
    help_needed = st.checkbox("Need Help?")

    if st.button("Submit Update"):
        new_entry = pd.DataFrame([{
            "Date": str(today),
            "Team": team,
            "Participant": participant,
            "Update": update,
            "Challenges": challenges,
            "Help Needed": help_needed
        }])
        df = pd.read_csv("data/daily_progress.csv")
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv("data/daily_progress.csv", index=False)
        st.success("Submitted successfully!")

    st.subheader("Summary of Today's Updates")
    df = pd.read_csv("data/daily_progress.csv")
    daily_updates = df[df["Date"] == str(today)]

    if not daily_updates.empty:
        prompt = f"Summarize the following progress updates for {today}:\n\n"
        for _, row in daily_updates.iterrows():
            prompt += f"- {row['Participant']}: {row['Update']}\n"

        try:
            summary = groq_chat_completion(prompt)
            st.markdown("### Summary:")
            st.write(summary)
        except Exception as e:
            st.error("Error generating summary.")
    else:
        st.info("No updates found for this date.")