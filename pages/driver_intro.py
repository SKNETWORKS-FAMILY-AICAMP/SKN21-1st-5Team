'''
작성자: 김가람
날짜: 2025-10-23
'''
import streamlit as st
import pandas as pd
from sql.drivers import DriversDBManager
from data.driver import DriverData

# 이미지 crop 모듈
from PIL import Image

def load():
    st.set_page_config(page_title="레이서 목록", page_icon="🚗")

    driversDB = DriversDBManager()

    team_list = driversDB.select_teams()

    cols = st.columns(2)  # 한 줄에 2개씩   

    for t in team_list:
        team_name = t[0]
        st.subheader(team_name)

        driver_list = driversDB.select_drivers_by_team(team_name)
        
        col1, col2 = st.columns(2)

        for i in range(0, len(driver_list)):
            data: DriverData = driver_list[i]

            col = (col1 if i%2 == 0 else col2)
            
            with col:
                card_view(data)

def card_view(data: DriverData):
    st.image(data.img, width=100)
    with st.container(border=True):
        sub_col1, sub_col2 = st.columns([1, 2])
        with sub_col1:
            country_file_name = data.country.lower().replace(" ", "_")
            st.image(f"data/flag/{country_file_name}.png", width=25)
        with sub_col2:
            st.write(f"**{data.name}**")

if __name__ == "__main__":
    load()