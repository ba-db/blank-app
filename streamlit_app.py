import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# Define the pages and their associated functions
pages = ["Properties", "More data"]
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Set the logo text and styles for the navbar
logo_text = "Melbourne Property Price Estimator"

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "justify-content": "right",
        "padding-left": "0rem",
        "padding-right": "0rem",
    },
    "div": {
        "max-width": "32rem",
    },
    "ul": {
        "justify-content": "right",
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

# Display the title with large text
st.markdown(f"<h1 style='text-align: left;'>{logo_text}</h1>", unsafe_allow_html=True)

# Add icons with corresponding text
pages_with_icons = [
    ("🏡 Properties", "Properties"),
    ("📊 More data", "More data"),
]

# Create a navbar with icons
page = st_navbar(
    [name for icon, name in pages_with_icons],
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
