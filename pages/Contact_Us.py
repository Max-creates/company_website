import streamlit as st
import pandas as pd
from send_email import send_email

df = pd.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    select_box = st.selectbox("What topic do you want to discuss?", df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {select_box}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")

    