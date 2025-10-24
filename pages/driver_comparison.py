import streamlit as st
import pandas as pd
from sql.drivers import DriversDBManager
from data.driver import DriverData

st.set_page_config(page_title="F1 Drivers", page_icon="data/logo.png")
st.logo("data/logo.png")


col1, col2 = st.columns([1, 1])

driversDB = DriversDBManager()
driver_list: list[DriverData] = driversDB.select_drivers()

for driver in driver_list:
    country_file_name = driver.country.lower().replace(" ", "_")
    d = (driver.name, driver.team, country_file_name, driver.img)
    st.text(d)
    st.image(f"data/flag/{country_file_name}.png", width=25)
    st.image(driver.img)

