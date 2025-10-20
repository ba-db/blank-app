import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# Define the pages and their associated functions
pages = [("🏡 Properties", "Properties"), ("📊 More data", "More data")]
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Set the logo text and styles for the navbar
logo_text = "Melbourne Property Price Estimator"

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "display": "flex",
        "align-items": "center",
        "padding": "0.5rem",
    },
    "title": {
        "font-size": "1.5rem",
        "color": "rgb(49, 51, 63)",
        "margin-right": "auto",
    },
    "ul": {
        "display": "flex",
        "align-items": "center",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
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

# Custom render for title and navbar in one row
st.markdown(f"<div style='display: flex; align-items: center;'><h1 style='margin: 0;'>{logo_text}</h1></div>", unsafe_allow_html=True)

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
