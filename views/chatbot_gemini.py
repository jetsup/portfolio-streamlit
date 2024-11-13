import streamlit as st
import google.generativeai as genai
from helpers.utils import stream_data

genai.configure(api_key=st.secrets["gemini_api_key"])
model = genai.GenerativeModel("gemini-1.5-flash")

if "prompts" not in st.session_state:
    st.session_state["prompts"] = []
prompt_user = "user"
prompt_ai = "ai"

ABOUT_ME_CONTEXT = """
My name is George Ngigi. I have a Bachelor of Science in Computer Technology from Murang'a University of Technology.
Professionally, I am a software developer and robotics enthusiast. I have been developing software and coding since 2018.
I have specialized in desktop development using Java and Python, web development using Django and Laravel, and embedded systems development using STM32, ESP-IDF, and Arduino.
For android development, I am proficient with Java programming language but I am still learning Kotlin.
You can find some of my projects in my [GitHub](https://www.github.com/jetsup).
I am also a robotics enthusiast and have experience in developing robotic systems using ROS, OpenCV, and Raspberry Pi.
"""

def call_gemini(prompt: str) -> str:
    response = model.generate_content(f"Only give precise answers and always in first person.\nGiven the context:\n{ABOUT_ME_CONTEXT}\n\nUser: {prompt}")
    return response.text if response.text else "I'm sorry, I don't understand the question."


prompt = st.chat_input("Say something")

if prompt:
    st.session_state.prompts.append({"by": prompt_user, "prompt": prompt})

    for prompt in st.session_state.prompts:
        with st.chat_message(prompt["by"]):
            st.write(prompt["prompt"])

    with st.chat_message("ai"):
        SAMPLE_RESPONSE = "Hello! I'm a chatbot that can help you with any questions you have about George Ngigi. This is a sample response."
        ai_response = call_gemini(prompt)
        st.write_stream(stream_data(ai_response))
        st.session_state.prompts.append({"by": prompt_ai, "prompt": ai_response})
