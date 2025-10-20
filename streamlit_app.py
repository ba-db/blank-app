
import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


pages = ["Properties", "More data"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
styles = {
    "nav": {
        "background-color": "green",
        "justify-content": "right",
    },
    "span": {
        "color": "white",
        "padding": "2px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "2px",
    }
}
options = {
    "show_menu": False,
}

page = st_navbar(
    pages,
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
