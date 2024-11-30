import streamlit as st
import smmap,ssl
from send_email import send_email

st.header('I would love to hear from you'.title())

with st.form(key='email_form'):

    user_email = st.text_input('Your email address')
    user_message = st.text_area('Your Message')

    message = f"""Subject: Web Forms

{user_message}

From: {user_email}

    """

    button = st.form_submit_button('Submit')

    if button:
        send_email(message=message)