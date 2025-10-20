
import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


pages = ["Properties", "More data"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_text = "Melbourne Property Price Estimator"
logo_path = None
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

col1, col2 = st.columns([1,4])
with col1:
    st.markdown(
        f"<div style='font-size:20px; font-weight:600; color:#31333F; padding:8px 12px;'>{logo_text}</div>",
        unsafe_allow_html=True,
    )
with col2:
    page = st_navbar(
        pages,
        logo_path=logo_path,
        styles=styles,
        options=options,
    )


functions = {
    "Properties": pg.show_properties,
    "More data": pg.show_data,
}
go_to = functions.get(page)
if go_to:
    go_to()