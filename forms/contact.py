import streamlit as st
from utils import send_email, is_email_valid

def contact_form():
    with st.form("contact_form"):
        st.write("Please fill out the form below to get in touch with me.")
        name = st.text_input("Name", autocomplete="name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if is_email_valid(email):
                if send_email(name, email, subject, message):
                    st.success("Message sent successfully!")
                else:
                    st.error("An error occurred. Please try again.")
                    print("An error occurred. Please try again.")
                    st.stop()
            else:
                st.error("Please enter a valid email address.")
                print("Please enter a valid email address.")
                st.stop()
