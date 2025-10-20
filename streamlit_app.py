import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

# --- Define SVG icons (inline so no files needed) ---
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

# --- Inject custom CSS for layout and scaling ---
st.markdown("""
<style>
/* Layout the title and nav bar on one green strip */
.navbar-container {
    background-color: rgb(123, 209, 146);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.4rem 1rem;
    border-radius: 0.5rem;
}
.navbar-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: rgb(49,51,63);
}

/* Style for icons and labels in nav */
.nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 0.9rem;
    line-height: 1.2;
}
.nav-item svg {
    width: 32px;
    height: 32px;
    margin-bottom: 0.2rem;
}
.nav-label {
    color: rgb(49,51,63);
}
</style>
""", unsafe_allow_html=True)

# --- Render title bar ---
st.markdown("""
<div class="navbar-container">
    <div class="navbar-title">Melbourne Property Price Estimator</div>
    <div id="custom-nav"></div>
</div>
""", unsafe_allow_html=True)

# --- Navigation styles (align right) ---
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "justify-content": "right",
        "padding-left": "0rem",
        "padding-right": "0rem",
    },
    "div": {"max-width": "32rem"},
    "ul": {"justify-content": "right"},
    "span": {
        "border-radius": "0.5rem",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {"background-color": "rgba(255, 255, 255, 0.25)"},
    "hover": {"background-color": "rgba(255, 255, 255, 0.35)"},
}

# --- Show navbar ---
page = st_navbar(pages, styles=styles, options={"show_menu": True})

# --- Page mapping (strip HTML tags by index) ---
functions = {
    pages[0]: pg.show_properties,
    pages[1]: pg.show_data,
}
go_to = functions.get(page)
if go_to:
    go_to()
