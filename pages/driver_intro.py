'''
작성자: 김가람
날짜: 2025-10-23
'''
import streamlit as st
import pandas as pd
from sql.drivers import DriversDBManager

st.set_page_config(page_title="레이서 목록", page_icon="🚗")

driversDB = DriversDBManager()

team_list = driversDB.select_teams()

cols = st.columns(2)  # 한 줄에 2개씩   

for t in team_list:
    team_name = t[0]
    st.subheader(team_name)

    driver_list = driversDB.select_drivers_by_team(team_name)
    for i in range(0, len(driver_list), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(driver_list):
                with col:
                    with st.container(border=True):
                        d = driver_list[i + j]
                        country_file_name = d[2].lower().replace(" ", "_")
                        st.image(f"data/flag/{country_file_name}.png", width=25)
                        st.link_button(f"**{d[0]}**", "#")