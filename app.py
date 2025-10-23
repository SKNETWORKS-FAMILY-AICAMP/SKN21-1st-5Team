'''
작성자: 김가람
날짜: 2025-10-22
'''
import streamlit as st
from sql import drivers

st.set_page_config(page_title="F1 Drivers", page_icon="data/logo.png")
st.logo("data/logo.png")

year = st.selectbox(
    label = "년도 선택",
    options = range(2020, 2030),
    index = 5
)

st.title(f"F1 Drivers {year}")
st.image("data/logo.png")
# st.button("test", on_click=drivers.select_team)
# st.sidebar.page_link("pages/player_intro.py", label="Home", icon='🏠')

