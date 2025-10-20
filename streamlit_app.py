import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# Pages with icons above text
pages = [
    "🏠\nProperties",
    "📈\nMore data"
]

# Define styles
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "display": "flex",
        "align-items": "center",
        "justify-content": "space-between",
        "padding": "0.5rem 1rem",
    },
    "div": {
        "display": "flex",
        "align-items": "center",
        "justify-content": "flex-end",
        "flex-grow": "1",
    },
    "ul": {
        "justify-content": "flex-end",
        "flex-grow": "1",
        "margin": "0",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.25rem",
        "padding": "0.4375rem 0.625rem",
        "text-align": "center",
        "white-space": "pre-line",  # puts emoji above text
        "font-size": "0.9rem",
        "font-weight": "500",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

# Custom HTML to inject the title into the navbar
title_html = """
<style>
.navbar-container {
    background-color: rgb(123, 209, 146);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.4rem 1rem;
    border-radius: 0.5rem;
}
.navbar-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: rgb(49, 51, 63);
}
</style>
<div class="navbar-container">
    <div class="navbar-title">Melbourne Property Price Estimator</div>
    <div id="custom-nav"></div>
</div>
"""

# Inject the title bar
st.markdown(title_html, unsafe_allow_html=True)

# Render the navigation bar aligned right (in the #custom-nav)
page = st_navbar(
    pages,
    styles=styles,
    key="navbar",
    options={"show_menu": True},
)

# Map navigation to page functions
functions = {
    "🏠\nProperties": pg.show_properties,
    "📈\nMore data": pg.show_data,
}

if page in functions:
    functions[page]()
