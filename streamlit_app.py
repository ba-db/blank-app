import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# --- Define your pages ---
pages = [
    "🏠\nProperties",
    "📈\nMore Data"
]

# --- Title text ---
logo_text = "Melbourne Property Price Estimator"

# --- Inject CSS for style and icons ---
st.markdown("""
<style>
/* Navbar container with new coral background */
.navbar-container {
    background-color: #FFA9A3; /* soft coral tone */
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.6rem 1.2rem;
}

/* Title on the left */
.navbar-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2B2B2B;
}

/* Align icons and text vertically */
[data-testid="stHorizontalBlock"] ul li span {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: pre-line !important;
    line-height: 1.2;
    text-align: center;
}

/* Make the emoji icons larger (only the first line) */
[data-testid="stHorizontalBlock"] ul li span::first-line {
    font-size: 2.4rem;  /* adjust this to make icons bigger */
}

/* Text under icons */
[data-testid="stHorizontalBlock"] ul li span {
    font-size: 0.9rem !important;
    font-weight: 600 !important;
    color: #FF6F61 !important; /* coral accent for icons and text */
}

/* Active tab */
[data-testid="stHorizontalBlock"] ul li[data-active="true"] span {
    color: #2B2B2B !important; /* dark text when active */
}

/* Hover effect */
[data-testid="stHorizontalBlock"] ul li:hover span {
    opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)

# --- Navbar title layout ---
st.markdown(f"""
<div class="navbar-container">
    <div class="navbar-title">{logo_text}</div>
</div>
""", unsafe_allow_html=True)

# --- Navbar styles (keep right alignment) ---
styles = {
    "nav": {
        "background-color": "#FFA9A3",  # coral background
        "justify-content": "right",
        "padding-left": "0rem",
        "padding-right": "0rem",
    },
    "ul": {"justify-content": "right"},
    "span": {
        "border-radius": "0.5rem",
        "margin": "0 0.25rem",
        "padding": "0.4375rem 0.625rem",
        "text-align": "center",
        "white-space": "pre-line",
    },
    "active": {"background-color": "rgba(255, 255, 255, 0.4)"},
    "hover": {"background-color": "rgba(255, 255, 255, 0.2)"},
}

options = {"show_menu": True}

# --- Show navbar ---
page = st_navbar(
    pages,
    styles=styles,
    options=options,
)

# --- Page routing ---
functions = {
    "🏠\nProperties": pg.show_properties,
    "📈\nMore Data": pg.show_data,
}
go_to = functions.get(page)
if go_to:
    go_to()
