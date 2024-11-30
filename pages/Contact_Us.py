import streamlit as st
import pandas as pd
from send_email import send_email

st.header("Let's Talk".title())

with st.form(key='email_form'):

    user_email = st.text_input('Your email address')
    contact_reason = st.selectbox('Your Reason for Contact',('Collaboration','Recruitment','Other'))
    user_message = st.text_area('Your Message')

    message = f"""Subject: Web Forms

Contact Reason: {contact_reason}

{user_message}

From: {user_email}

    """

    button = st.form_submit_button('Submit')

    if button:
        send_email(message=message)
        st.info('Email Sent Successfully!')