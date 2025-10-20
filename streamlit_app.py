import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# Define the pages and their associated functions
pages = [("🏡 Properties", "Properties"), ("📊 More data", "More data")]
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Set the logo text
logo_text = "Melbourne Property Price Estimator"

# Styles for the navbar
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "display": "flex",
        "align-items": "center",
        "padding": "0.5rem",
    },
    "div": {
        "max-width": "32rem",
    },
    "ul": {
        "display": "flex",
        "align-items": "center",
        "list-style": "none",
        "margin": "0",
        "padding": "0",
    },
    "li": {
        "margin": "0 1rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

options = {
    "show_menu": True,
}

# Display title above the navbar
st.markdown(f"<h1 style='text-align: left; margin: 0;'>{logo_text}</h1>", unsafe_allow_html=True)

# Create a navbar with icons
page = st_navbar(
    [name for icon, name in pages],
    styles=styles,
    options=options,
)

# Map the page names to their respective functions
functions = {
    "Properties": pg.show_properties,
    "More data": pg.show_data,
}

# Execute the function corresponding to the selected page
go_to = functions.get(page)
if go_to:
    go_to()
