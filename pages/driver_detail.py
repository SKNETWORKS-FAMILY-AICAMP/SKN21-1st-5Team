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
            
            sub_col3, sub_col4 = st.columns([1, 1])
            
            with sub_col3:
                st.subheader("2025")
                
                st.metric(
                    label="Season Position",
                    value=str(stats.season_position),           # 출력할 값
                )

                st.metric(
                    # label=":blue[온도 ]",   # header/title. markdown, 이모지 shortcode, latex($, $$ 로 감싼다.), color text지원.
                    label="Season Points",
                    value=str(stats.season_points),           # 출력할 값
                    delta="0"           # metric의 등락 크기값(옵션). `+` 로 시작하거나 생략하면 오름, `-` 로 시작하면 내림.
                )
            with sub_col4:
                st.subheader("CAREER STATS")

                st.metric(
                    label="Grand Prix Entered",
                    value=str(career.grand_prix_entered),           # 출력할 값
                )

                st.metric(
                    # label=":blue[온도 ]",   # header/title. markdown, 이모지 shortcode, latex($, $$ 로 감싼다.), color text지원.
                    label="Career Points",
                    value=str(career.career_points),           # 출력할 값
                    delta="0"           # metric의 등락 크기값(옵션). `+` 로 시작하거나 생략하면 오름, `-` 로 시작하면 내림.
                )
