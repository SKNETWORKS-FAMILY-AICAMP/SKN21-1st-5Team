'''
작성자: 김가람
날짜: 2025-10-23
'''
import streamlit as st
from data.connect import WebConnectManager

wm = WebConnectManager()

for v in wm.get_drivers():
    # name = (v[1] + "-" + v[0]).lower()
    # driver = wm.get_driver(name)
    st.text(v)