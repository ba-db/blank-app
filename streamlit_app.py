
import os
import base64
import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


HOUSE_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" fill="rgb(49,51,63)">
<path d="M5 19V9l7-5 7 5v10h-5v-6H10v6H5z"/>
</svg>
"""

GRAPH_ICON = """
<svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" fill="rgb(49,51,63)">
<path d="M3 17h2v-7H3v7zm4 0h2V7H7v10zm4 0h2v-4h-2v4zm4 0h2V4h-2v13zm4 0h2V10h-2v7z"/>
</svg>
"""

# --- Define pages with HTML icons above text ---
pages = [
    f"<div class='nav-item'>{HOUSE_ICON}<div class='nav-label'>Properties</div></div>",
    f"<div class='nav-item'>{GRAPH_ICON}<div class='nav-label'>More data</div></div>",
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
    pages[0]: pg.show_properties,
    pages[1]: pg.show_data,
}


go_to = functions.get(page)
if go_to:
    go_to()