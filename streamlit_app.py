
import os
import base64
import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


pages = [
    "🏠\nProperties",
    "📈\nMore data"
]
parent_dir = os.path.dirname(os.path.abspath(__file__))

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

page = st_navbar(
    pages,
    styles=styles,
    options=options,
)



functions = {
    "🏠\nProperties": pg.show_properties,
    "📈\nMore data": pg.show_data,
}
go_to = functions.get(page)
if go_to:
    go_to()