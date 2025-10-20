
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

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="360" height="36" viewBox="0 0 360 36">
  <style>
    .title {{ font-family: Arial, Helvetica, sans-serif; font-size:16px; fill:#31333F; font-weight:600; }}
  </style>
  <text x="0" y="22" class="title">{logo_text}</text>
</svg>'''
svg_b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
logo_path = f"data:image/svg+xml;base64,{svg_b64}"

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
    logo_path=logo_path,
    logo_page=None,       # or set to pages[0] to make the logo clickable
    styles=styles,
    options=options,
    default=pages[0],
)



functions = {
    "🏠\nProperties": pg.show_properties,
    "📈\nMore data": pg.show_data,
}
go_to = functions.get(page)
if go_to:
    go_to()