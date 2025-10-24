import streamlit as st
from sql.drivers import DriversDBManager
from data.driver import DriverData

st.set_page_config(page_title="F1 Drivers", page_icon="data/logo.png")
st.logo("data/logo.png")


col1, col2 = st.columns([1, 1])

driversDB = DriversDBManager()
driver_list: DriverData = driversDB.select_drivers()

st.text(driver_list)
