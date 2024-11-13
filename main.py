import streamlit as st

home_page = st.Page(
    page="views/home.py",
    title="Home",
    icon="🏠",
    # default=True,
)

about_page = st.Page(
    page="views/about.py",
    title="About",
    icon="❔",
    default=True,
)

projects_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon="📂",
)

hobbies_page = st.Page(
    page="views/hobbies.py",
    title="Hobbies",
    icon="🎨",
)

my_journey_page = st.Page(
    page="views/my_journey.py",
    title="My Journey",
    icon="🚀",
)

about_chatbot_page = st.Page(
    page="views/chatbot_gemini.py",
    title="Chatbot",
    icon="🤖",
)

pg = st.navigation(
    {
        "Home": [about_page, about_chatbot_page],
        "Projects and Hobbies": [projects_page, hobbies_page, my_journey_page],
    }
)

pg.run()
