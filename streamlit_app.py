
import os
import base64
import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg


pages = ["Properties", "More data"]
parent_dir = os.path.dirname(os.path.abspath(__file__))

logo_text = "Melbourne Property Price Estimator"

def make_text_svg(text, font_size=18, fill="#31333F", padding=8, height=40, width=400):
    return f"""<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}'>
  <rect width='100%' height='100%' fill='none'/>
  <text x='{padding}' y='{int(height*0.65)}' font-family='Inter, Arial, sans-serif' font-size='{font_size}' fill='{fill}' font-weight='600'>{text}</text>
</svg>"""

# schrijf SVG naar bestand (st_navbar verwacht een pad naar een bestand)
svg_path = os.path.join(parent_dir, "logo.svg")
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(make_text_svg(logo_text, font_size=18, fill="#31333F", height=40))

logo_path = svg_path
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