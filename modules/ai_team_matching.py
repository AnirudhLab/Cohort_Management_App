import streamlit as st
import pandas as pd
import requests
import toml
import os

def show():
    st.title("🤖 AI Team Matching (Manual Secret Loader)")

    if st.session_state.get("user_role") != "admin":
        st.error("Admins only.")
        return

    # Load secrets manually
    try:
        secrets = toml.load(".streamlit/secrets.toml")
        api_key = secrets["GROQ_API_KEY"]
        st.success(f"GROQ Key loaded: {api_key[:5]}...")
    except Exception as e:
        st.error("Error loading GROQ API Key")
        st.exception(e)
        return

    st.markdown("### ✅ Testing /v1/models from GROQ API")
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        res = requests.get("https://api.groq.com/openai/v1/models", headers=headers)
        if res.status_code == 200:
            models = res.json()["data"]
            st.success(f"{len(models)} models available")
            st.write([m["id"] for m in models])
        else:
            st.error(f"Groq API returned {res.status_code}")
            st.text(res.text)
            return
    except Exception as e:
        st.error("GROQ API test failed")
        st.exception(e)
        return

    # Team generation (fake)
    df = st.session_state.participants_df
    df = df[df["Status"] == "Approved"].copy()
    if df.empty:
        st.warning("No approved participants.")
        return

    num = st.number_input("Number of teams", min_value=2, max_value=10, value=3)
    if st.button("Generate Teams"):
        try:
            df = df.sample(frac=1).reset_index(drop=True)
            df["Team"] = [f"Team {i%num+1}" for i in range(len(df))]
            st.dataframe(df)
        except Exception as e:
            st.error("🚨 Error generating teams.")
            st.exception(e)