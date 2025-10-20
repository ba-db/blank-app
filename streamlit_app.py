import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# Define pages with icons above text (using emoji or Unicode icons)
pages = [
    "🏠\nProperties",
    "📈\nMore data"
]

# Parent directory (optional, depending on your structure)
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Navbar title
title_html = """
<div style="
    font-size: 1.8rem; 
    font-weight: 700; 
    color: #31333F; 
    display: flex; 
    align-items: center; 
    gap: 0.5rem;
">
    <span>Melbourne Property Price Estimator</span>
</div>
"""

# Display the title in the navbar area
st.markdown(
    f"""
    <div style='
        display: flex; 
        align-items: center; 
        justify-content: space-between; 
        background-color: rgb(123, 209, 146); 
        padding: 0.6rem 1rem; 
        border-radius: 0.5rem;
    '>
        {title_html}
    </div>
    """,
    unsafe_allow_html=True
)

# Navbar styles
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "justify-content": "center",
        "padding-left": "0rem",
        "padding-right": "0rem",
    },
    "div": {
        "max-width": "32rem",
    },
    "ul": {
        "justify-content": "center",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
        "text-align": "center",
        "white-space": "pre-line",  # allows emoji above text
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

# Show navbar
page = st_navbar(
    pages,
    styles=styles,
    options={"show_menu": True},
)

# Map functions to pages (remove emoji+newline)
page_mapping = {
    "🏠\nProperties": pg.show_properties,
    "📈\nMore data": pg.show_data,
}

if page in page_mapping:
    page_mapping[page]()
