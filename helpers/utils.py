import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from time import sleep

def send_email(name: str, email: str, subject: str, message: str) -> bool:
    body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = st.secrets["smtp_email_handling_email"]
    # Add a reply-to header so that you can reply to the email directly
    msg.add_header('Reply-To', email)

    try:
        with smtplib.SMTP(st.secrets["smtp_email_handling_server"], 587) as server:
            server.starttls()
            server.login(st.secrets["smtp_email_handling_email"], st.secrets["smtp_email_handling_password"])
            server.sendmail(email, st.secrets["smtp_email_handling_email"], msg.as_string())
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        return False

def send_confirmation_email(email, subject, message) -> bool:
    body = f"Thank you for contacting me. I have received your message and will get back to you as soon as possible."
    
    msg = MIMEText(body)
    msg["Subject"] = "Message Received"
    msg["From"] = st.secrets["smtp_email_handling_email"]
    msg["To"] = email

    try:
        with smtplib.SMTP(st.secrets["smtp_email_handling_server"], 587) as server:
            server.starttls()
            server.login(st.secrets["smtp_email_handling_email"], st.secrets["smtp_email_handling_password"])
            server.sendmail(st.secrets["smtp_email_handling_email"], email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        return False

def is_email_valid(email: str):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def stream_data(str_data: str):
    for letter in str_data:
        yield letter
        sleep(0.02)
