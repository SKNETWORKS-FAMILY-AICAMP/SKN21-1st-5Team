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

st.markdown("""
   <style>
   /* Keyframe for fade-in */
   @keyframes fadeInTitle {
       from {opacity: 0; transform: translateY(-10px);}
   }  
            
   /* Apply animation to the custom title */
   .fade-title {
       font-size: 2.5em;
       font-weight: 700;
       text-align: center;
       color: #ff4b4b;
       animation: fadeInTitle 1.2 ease-in-out;
   }

   <style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="fade-title">FAST F1 페이지</h1>', unsafe_allow_html=True)

st.write("빨리빨리 F1 웹사이트에 오신것을 환영합니다. 원하시는 메뉴를 선택해 주세요")

st.image("https://www.grandprix247.com/wp-content/uploads/2025/04/f1-movie-brad-pitt-poster-750x400.jpg", caption="F1 Movie Poster Copyright © Apple Films 2025", use_container_width=True)

col1, col2, col3 = st.columns(3)

if col1.button('Main Menu'):
   st.switch_page("app.py") 

if col2.button('F1 운전자들'):
   st.switch_page("driver_intro.py")

if col3.button('F1 Driver Comparison'):
   st.switch_page("driver_comparison(test).py")

