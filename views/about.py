import streamlit as st
from PIL import Image, ImageOps, ImageDraw
from forms.contact import contact_form

column1, column2 = st.columns(2, gap="small", vertical_alignment="center")

def round_corners(image, radius):
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)

    return result

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
    
with column1:
    img = Image.open("assets/images/George Ngigi.jpg")
    radius = 3000
    rounded_img = round_corners(img, radius)
    st.image(rounded_img, width=300, caption="George Ngigi")

with column2:
    st.title("George Ngigi")
    st.markdown(
        """
        Software Developer and Robotics Enthusiasts, solving problems using code and electronics parts.
        """
    )
    if st.button("✉️ Contact me"):
        show_contact_form()

st.markdown('My name is :blue[George Ngigi]. I am a passionate software developer for :blue[desktop], :blue[android], :blue[web] and :blue[embedded systems]. I have specialized in **desktop development using Java and Python**, **web development using Django and Laravel**, and **embedded systems development using STM32, ESP-IDF, and Arduino**. For **android development, I am proficient with Java programming language** but I am still learning Kotlin, the defacto and official language. You can find some of my projects in my [GitHub](https://www.github.com/jetsup). I am also a robotics enthusiast and have experience in developing robotic systems using _ROS, OpenCV, and Raspberry Pi_.')
st.markdown("---")

# Experience, Education and Skills
st.header("Experience")
st.markdown(
    """
    - **Software Developer** at [NaiPrints](https://naiprints.co.ke/) (August - Present)
    - **Embedded Software Developer Intern** at Sagana Technology Research (2022 - 2024)
    """
)

st.header("Education")
st.markdown(
    """
    - **Bachelor of Science in Computer Technology** at [Murang'a Technology](https://www.mut.ac.ke/)
    - **High School** at Hero's High School
    """
)

st.header("Skills")
st.markdown(
    """
    - **Programming Languages**: Java, Python, C++, JavaScript, PHP, SQL
    - **Frameworks**: [Django](https://www.djangoproject.com/), [Laravel](https://laravel.com/), [Spring Boot](https://spring.io/projects/spring-boot)
    - **Tools**: [Git](https://git-scm.com/), [Docker](https://www.docker.com/)
    - **Other**: [ROS](https://www.ros.org), [OpenCV](https://opencv.org/), [Raspberry Pi](https://www.raspberrypi.com/), [STM32](https://www.st.com), [ESP-IDF](https://idf.espressif.com/), [Arduino](https://www.arduino.cc)
    """
)
