'''
작성자: 김가람
날짜: 2025-10-23
'''
import streamlit as st
import re
from sql.drivers import DriversDBManager
from data.driver import DriverData

def load():
    st.subheader("레이서 검색")
    name_value = st.text_input("이름")

    if name_value:
        if re.fullmatch(r"[A-Za-z0-9]+", name_value):        
            driversDB = DriversDBManager()

            result = driversDB.select_driver_by_keyword(name_value)
            
            for d in result:
                data: DriverData = d
                col1, col2, col3 = st.columns([1, 2, 2])
                with col1:
                    country_file_name = data.country.lower().replace(" ", "_")
                    st.image(f"data/flag/{country_file_name}.png", width=25)
                with col2:
                    st.text(data.team)
                with col3:
                    st.text(data.name)
        else:   
            st.markdown("<span style='color:red'>❌ 영어 이외의 문자가 포함되어 있습니다.</span>", unsafe_allow_html=True)

if __name__ == "__main__":
    load()

