import streamlit as st
from PIL import Image
# import firebase_admin
# from firebase_admin import auth
import base64
import io
from stickyhelper import st_fixed_container
video_file = open('Videos/clothed_video_main.mp4', 'rb')
video_bytes = video_file.read()


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_base64_video(video_path):
    with open(video_path, 'rb') as video_file:
        video_bytes = video_file.read()
    return base64.b64encode(video_bytes).decode()

def get_image_html(image_path, width=575):
    img_base64 = get_base64_of_bin_file(image_path)
    html_code = f"""
    <img id="logo" class="logo"
         src="data:image/png;base64,{img_base64}"
         style="width: {width}px; display: block; margin-left: auto; margin-right: auto;">
    """
    return html_code


# ---- Set page config ----
st.set_page_config(page_title="BridgeSign", layout="wide")

# ---- CUSTOM CSS for background and button styling ----
# ---- CUSTOM CSS for background and button styling ----
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #f7f5ed;
    }

    /* Button styles */
    div.stButton > button {
        background-color: #ffe9a5;
        color: black;
        border: none;
        padding: 0.75em 2em;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold; /* <-- good */
        width: 200px;
        margin: 0 auto;
        display: block;
    }
    div.stButton > button:hover {
        background-color: #4dbbf4;
        color: black;
    }
    .mission-button > button {
        background-color: #0277b5;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold; /* <-- make sure this is kept too */
        width: 40%;
        min-width: 150px;
        max-width: 200px;
        margin-top: 1em;
        margin-left: auto;
        margin-right: auto;
        display: block;
        cursor: pointer;
    }
    .mission-button > button:hover {
        background-color: #4dbbf4;
        color: white;
    }
    /* Initial logo styling */
    #logo {
        width: 575px;
        transition: all 0.6s ease-in-out; /* Smooth resizing and moving */
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    /* Sticky logo when you scroll */
    #logo.sticky {
        position: fixed;
        top: 10px;
        left: 50%;
        transform: translateX(-50%) scale(0.5);
        transition: all 0.6s ease-in-out;
        animation: bounce 0.4s ease;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        border-radius: 12px;
    }
    @keyframes bounce {
        0%   { transform: scale(1); }
        50%  { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    /* Fade in animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .fade-in {
        animation: fadeIn 1.2s ease-in forwards;
    }

    .fade-in-slow {
        opacity: 0; /* Start invisible */
        animation: fadeIn 1.8s ease-in forwards;
        animation-delay: 0.5s;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# with st_fixed_container(mode="fixed", position="top", border=True, horizontal_position="right", key="top_right"):
#     if st.button("Sign Up", key="signup_button"):
#         st.switch_page("pages/sign_up.py")

#     if st.button("Login", key="login_button"):
#         st.switch_page("pages/log_in.py")

# with st_fixed_container(mode="fixed", position="top", border=True, horizontal_position="left", key="top_left"):
#     if st.button("Resources", key="signup_button1"):
#         st.switch_page("pages/sign_up.py")

#     if st.button("About Us", key="login_button2"):
#         st.switch_page("pages/mission.py")



# ---- Add vertical space before buttons ----
st.markdown("<br><br>", unsafe_allow_html=True)

# ---- Centered Call to Action: SIGN UP and LOGIN Buttons ----
col1, col2, col3 = st.columns([1.5, 3, 1.5])

with col1:
    if st.button("Resources", key="signup_button1"):
        st.switch_page("pages/sign_up.py")

    if st.button("About Us", key="login_button2"):
        st.switch_page("pages/mission.py")


    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)

    st.image("pictures/minihands3.png", use_container_width=True)
    st.image("pictures/minihands4.png", use_container_width=True)
    st.image("pictures/minihands3.png", use_container_width=True)
    st.image("pictures/minihands4.png", use_container_width=True)


with col2:
    st.markdown(get_image_html("pictures/big_logo.png"), unsafe_allow_html=True)

    st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        <h1 class="fade-in" style='text-align: center; color: #0277b5;'>
            The AI Sign Language Trainer for Healthcare
        </h1>
        <h4 class="fade-in-slow" style='text-align: center; color: #2aaaff;'>
            An interactive platform helping professionals build essential ASL skills through AI-driven practice.
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    video_base64 = get_base64_video('Videos/clothed_video_main.mp4')

    st.markdown(
        f"""
        <div class="fade-in-slow" style="text-align: center;">
            <video width="500" autoplay loop muted playsinline>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown(
        """
        <h5 class="fade-in-slow" style='text-align: center; color: #2aaaff;'>
            According to the 2021 American Community Survey (ACS), about 3.6%% of the U.S. population,
            or about 11 million individuals, consider themselves deaf or have serious difficulty hearing.
        </h5>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h5 class="fade-in-slow" style='text-align: center; color: #2aaaff;'>
            The Hearing Loss Association of America estimates that 48 million Americans have some degree
            of hearing loss.
        </h5>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h5 class="fade-in-slow" style='text-align: center; color: #2aaaff;'>
            Over 500,000 people in America use ASL as their native language.
        </h5>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h5 class="fade-in-slow" style='text-align: center; color: #2aaaff;'>
            Currently there are only 10,000 licensed translators for ASL in America.
        </h5>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='mission-button' style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Our Mission", key="mission_button"):
        st.switch_page("pages/mission.py")

    st.markdown("</div>", unsafe_allow_html=True)

with col3:

    if st.button("Sign Up", key="signup_button"):
        st.switch_page("pages/sign_up.py")

    if st.button("Login", key="login_button"):
        st.switch_page("pages/log_in.py")

    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)
    # st.markdown("<br>", unsafe_allow_html=True)

    st.image("pictures/minihands3.png", use_container_width=True)
    st.image("pictures/minihands4.png", use_container_width=True)
    st.image("pictures/minihands3.png", use_container_width=True)
    st.image("pictures/minihands4.png", use_container_width=True)
