import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# --- Simple text pages (no HTML) ---
pages = ["Properties", "More data"]

# --- Title text ---
title_text = "Melbourne Property Price Estimator"

# --- Custom CSS for SVG icons ---
st.markdown("""
<style>
/* Whole navbar */
.navbar-container {
    background-color: rgb(123, 209, 146);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.4rem 1rem;
    border-radius: 0.5rem;
}

/* Title on the left */
.navbar-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: rgb(49, 51, 63);
}

/* Navigation icon and label container */
[data-testid="stHorizontalBlock"] ul li span {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    color: rgb(49,51,63) !important;
}

/* House icon for Properties */
[data-testid="stHorizontalBlock"] ul li:nth-child(1) span:before {
    content: '';
    display: block;
    width: 30px;
    height: 30px;
    margin-bottom: 0.2rem;
    background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' fill='rgb(49,51,63)' viewBox='0 0 24 24'><path d='M5 19V9l7-5 7 5v10h-5v-6H10v6H5z'/></svg>") no-repeat center;
    background-size: contain;
}

/* Graph icon for More Data */
[data-testid="stHorizontalBlock"] ul li:nth-child(2) span:before {
    content: '';
    display: block;
    width: 30px;
    height: 30px;
    margin-bottom: 0.2rem;
    background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' fill='rgb(49,51,63)' viewBox='0 0 24 24'><path d='M3 17h2v-7H3v7zm4 0h2V7H7v10zm4 0h2v-4h-2v4zm4 0h2V4h-2v13zm4 0h2V10h-2v7z'/></svg>") no-repeat center;
    background-size: contain;
}
</style>
""", unsafe_allow_html=True)

# --- Render title ---
st.markdown(f"""
<div class="navbar-container">
    <div class="navbar-title">{title_text}</div>
</div>
""", unsafe_allow_html=True)

# --- Navbar styling ---
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
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
    },
    "active": {"background-color": "rgba(255, 255, 255, 0.25)"},
    "hover": {"background-color": "rgba(255, 255, 255, 0.35)"},
}

# --- Show navbar (no errors now) ---
page = st_navbar(pages, styles=styles, options={"show_menu": True})

# --- Map functions ---
functions = {
    "Properties": pg.show_properties,
    "More data": pg.show_data,
}

if page in functions:
    functions[page]()
