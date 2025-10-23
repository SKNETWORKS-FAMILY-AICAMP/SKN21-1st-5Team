import streamlit as st
from sql.drivers import DriversDBManager

st.set_page_config(page_title="F1 Drivers", page_icon="data/logo.png")
st.logo("data/logo.png")


col1, col2 = st.columns([1, 1])

driversDB = DriversDBManager()
driver_list = driversDB.select_drivers()

st.text(driver_list)

# with col1:
#     d = st.selectbox(
#         label = "레이서 선택",
#         options = driver_list
#     )

#     st.text(d)

# with col2:
#     d = st.selectbox(
#         label = "레이서 선택",
#         options = driver_list
#     )

#     st.text(d)
