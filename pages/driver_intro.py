'''
작성자: 김가람
날짜: 2025-10-23
'''
import streamlit as st
import pandas as pd
from sql.drivers import DriversDBManager
from data.driver import DriverData
import pages.driver_detail as detail

def load():
    st.set_page_config(page_title="레이서 목록", page_icon="🚗")

    driversDB = DriversDBManager()

    team_list = driversDB.select_teams()

    for t in team_list:
        team_name = t[0]
        st.subheader(team_name)

        driver_list = driversDB.select_drivers_by_team(team_name)
        
        for i in range(0, len(driver_list)):
            data: DriverData = driver_list[i]

            detail.card_view(data)

if __name__ == "__main__":
    load()
