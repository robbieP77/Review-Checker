from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


HTML_FILE = Path(__file__).with_name("Review Checker 3.6.5.html")

st.set_page_config(page_title="Review Checker 3.6.5", layout="wide")

if not HTML_FILE.is_file():
    st.error(f"Checker HTML file not found: {HTML_FILE.name}")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
