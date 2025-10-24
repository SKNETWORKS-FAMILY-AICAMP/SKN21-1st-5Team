'''
작성자: 김가람
날짜: 2025-10-23
'''
import streamlit as st
from sql.statistics import StatisticsDBManager
from data.driver import DriverData
from data.driver import Statistic
from data.driver import CareerStatistic

def card_view(data: DriverData):
    col1, col2 = st.columns([1,3])
    with col1:
        st.image(data.img)
    with col2:
        with st.container(border=True):
            sub_col1, sub_col2 = st.columns([1, 2])
            with sub_col1:
                country_file_name = data.country.lower().replace(" ", "_")
                st.image(f"data/flag/{country_file_name}.png", width=25)
            with sub_col2:
                st.write(f"**{data.name}**")

            
            statisticsDB = StatisticsDBManager()
            stats: Statistic = statisticsDB.select_season_stats_by_driver(data.name)
            career: CareerStatistic = statisticsDB.select_career_stats_by_driver(data.name)

            season_avg = statisticsDB.select_season_stats_aggr()
            career_avg = statisticsDB.select_career_stats_aggr()
            
            sub_col3, sub_col4 = st.columns([1, 1])
            
            with sub_col3:
                st.subheader("2025 Season")
                
                st.metric(
                    label="Season Position",
                    value=str(stats.season_position),
                    delta=(stats.season_position - season_avg["season_position"])
                )

                st.metric(
                    label="Season Points",
                    value=str(stats.season_points),
                    delta=(stats.season_points - season_avg["season_points"])
                )

                st.metric(
                    label="DNFs",
                    value=str(stats.dnfs),
                    delta=(stats.dnfs - season_avg["dnfs"])
                )
            with sub_col4:
                st.subheader("CAREER STATS")

                st.metric(
                    label="Grand Prix Entered",
                    value=str(career.grand_prix_entered),
                    delta=(career.grand_prix_entered - career_avg["grand_prix_entered"])
                )

                st.metric(
                    label="Career Points",
                    value=str(career.career_points),
                    delta=(career.career_points - career_avg["career_points"])
                )

                st.metric(
                    label="DNFs",
                    value=str(career.dnfs),
                    delta=(career.dnfs - career_avg["dnfs"])
                )
