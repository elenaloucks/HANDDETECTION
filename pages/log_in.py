# pages/log_in.py

import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import requests
import os

firebase_credentials = {
    "type": st.secrets["firebase"]["type"],
    "project_id": st.secrets["firebase"]["project_id"],
    "private_key_id": st.secrets["firebase"]["private_key_id"],
    "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
    "client_email": st.secrets["firebase"]["client_email"],
    "client_id": st.secrets["firebase"]["client_id"],
    "auth_uri": st.secrets["firebase"]["auth_uri"],
    "token_uri": st.secrets["firebase"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"],
    "universe_domain": st.secrets["firebase"]["universe_domain"],
}

cred = credentials.Certificate(firebase_credentials)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# ---- Page Config ----
st.set_page_config(page_title="Log In | BridgeSign", page_icon="🧏‍♀️", layout="wide")

# ---- CUSTOM CSS ----
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f7f5ed !important;
        animation: fadeInAnimation ease 1s;
        animation-iteration-count: 1;
        animation-fill-mode: forwards;
    }

    @keyframes fadeInAnimation {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .stButton>button {
        color: black !important;
        background: #ffe9a5 !important;
        border-radius: 8px !important;
        height: 3em !important;
        width: 100% !important;
        font-size: 1.2em !important;
        margin-top: 10px !important;
    }
    .stButton>button:hover {
        background: #ffd96b !important;
        color: black !important;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
        color: black !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        font-size: 1em !important;
    }
    label {
        color: #0077B6 !important;
        font-weight: bold !important;
    }
    /* NEW: Disable clicks on images */
    img {
        pointer-events: none;
    }
    </style>
    <script>
        window.scrollTo({top: 0, behavior: 'smooth'});
    </script>
    """,
    unsafe_allow_html=True
)

# ---- Layout ----
col1, col2, col3 = st.columns([1.5, 3, 1.5])

# ---- Left Column (small hand images) ----
with col1:
    st.image("pictures/minihands3.png", use_container_width=True)
    st.image("pictures/minihands4.png", use_container_width=True)

# ---- Middle Column (Login Form) ----
with col2:
    st.markdown(
        "<h1 style='color:#0077B6; text-align: center;'>Welcome Back!</h1>",
        unsafe_allow_html=True
    )

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    login_button = st.button("Log In")

    if login_button:
        try:
            firebase_api_key = st.secrets["firebase"]["api_key"]

            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={firebase_api_key}"

            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }

            response = requests.post(url, json=payload)
            result = response.json()

            if "idToken" in result:
                st.success("Login successful! 🎉 Redirecting...")
                st.session_state["user"] = result
                st.switch_page("pages/library.py")
            else:
                st.error(f"Login failed: {result.get('error', {}).get('message', 'Unknown error')}")

        except Exception as e:
            st.error(f"Login failed: {e}")

    if st.button("Back to Home", key="back_home_button_login"):
        st.switch_page("main.py")

# ---- Right Column (small hand images) ----
with col3:
    st.image("pictures/minihands3.png", use_container_width=True)
    st.image("pictures/minihands4.png", use_container_width=True)

# ---- Footer space ----
st.markdown("<br><br>", unsafe_allow_html=True)
