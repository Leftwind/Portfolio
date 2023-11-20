import streamlit as st
from send_email import send_email

st.header('Contact Me')

#They give e-mail, you get a mail with the content. 
with st.form(key='email_forms'):
    user_email = st.text_input('Your email adress')
    raw_message = st.text_area('Your message')
    message = f'''\
Subject: New email from {user_email}:
{raw_message}
From {user_email}
'''
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Your email was sent succesfully')