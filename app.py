'''
작성자: 김가람
날짜: 2025-10-22
'''
import streamlit as st
import pandas as pd 
import numpy as np
import time 

st.set_page_config(page_title="F1 Drivers", page_icon="data/logo.png")
st.logo("data/logo.png")

load = False

if not load:
   load = True

   home   = st.Page("pages/driver_dashboard.py", title="대시보드",   icon="🏠")
   intro   = st.Page("pages/driver_intro.py",  title="레이서 목록",   icon="🚗")
   search = st.Page("pages/driver_search.py",title="레이서 검색",   icon="🔍")
   repair = st.Page("pages/driver_comparison.py",title="레이서 비교",   icon="🆚")

   nav = st.navigation([home, intro, search, repair])
   nav.run()