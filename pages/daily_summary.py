import streamlit as st
import pandas as pd
from utils.groq_llm import groq_chat_completion

def show():
    st.title("Daily Progress Summary")

    today = st.date_input("Select Date")
    df = pd.read_csv("data/Daily_Progress.csv")
    daily_updates = df[df["Date"] == str(today)]

    if not daily_updates.empty:
        prompt = f"Summarize the following progress updates for {today}:\n\n"
        for _, row in daily_updates.iterrows():
            prompt += f"- {row['Participant']}: {row['Update']}\n"

        summary = groq_chat_completion(prompt)
        st.markdown("### Summary:")
        st.write(summary)
    else:
        st.info("No updates found for this date.")