'''
작성자: 김가람
날짜: 2025-10-22
'''

import streamlit as st
from web.connect import WebConnectManager

st.title('F1 Drivers 2025')

wm = WebConnectManager()

for v in wm.get_drivers():
    st.text(v)