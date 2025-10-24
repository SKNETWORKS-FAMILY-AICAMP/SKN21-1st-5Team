import streamlit as st
import pandas as pd 
import numpy as np
import time 

colA = st.columns(1)

if colA.button('English'):
   st.switch_page("drive_dashboard.py") 


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

st.markdown('<h1 class="fade-title">FAST F1 DATABASE</h1>', unsafe_allow_html=True)

st.write("Welcome to Fast F1 Website. Korea's very own fast service F1 Database. Please Select Your Menu")

st.image("https://www.grandprix247.com/wp-content/uploads/2025/04/f1-movie-brad-pitt-poster-750x400.jpg", caption="F1 Movie Poster Copyright © Apple Films 2025", use_container_width=True)

col1, col2, col3 = st.columns(3)

if col1.button('팀원 리스트'):
   st.switch_page("pages/driver_intro.py") 

if col2.button('선수 검색'):
   st.switch_page("pages/driver_search.py")

if col3.button('선수 기록 현황'):
   st.switch_page("pages/driver_comparison.py")

st.title("싸이트 소개")
st.write("저희의 F1선수들처럼, FAST F1 데이타 베이스는 F1경기와 선수들에 있어, 실시간으로 빠르고, 정확하고, 그리고 항상 신선한 특급 F1관련 정보를 제공하는 페이지 입니다. F1에 관련하여 열정있는 팬들분들게, 항상 F1관련된 정보를 빠르고 정확하게 드리고자 합니다.")
