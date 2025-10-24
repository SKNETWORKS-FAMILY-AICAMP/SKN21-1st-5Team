import streamlit as st
from sql.drivers import DriversDBManager
from data.driver import DriverData
from sql.statistics import StatisticsDBManager
from data.driver import Statistic
from data.driver import CareerStatistic

st.set_page_config(page_title="F1 Drivers", page_icon="data/logo.png")
st.logo("data/logo.png")

# col1, col2 = st.columns([1, 1])

driversDB = DriversDBManager()
driver_list: list[DriverData] = driversDB.select_drivers()
driver_name_list = [d.name for d in driver_list]


# for driver in driver_list:
#     country_file_name = driver.country.lower().replace(" ", "_")
#     d = (driver.name, driver.team, country_file_name, driver.img)
#     st.text(d)
#     st.image(f"data/flag/{country_file_name}.png", width=25)
#     st.image(driver.img)

if 'selected_racer1' not in st.session_state:
    st.session_state['selected_racer1'] = None
if 'selected_racer2' not in st.session_state:
    st.session_state['selected_racer2'] = None

# ------------------------------------------------------------
# 3. 레이서 선택 로직 (버튼 클릭 핸들러)
# ------------------------------------------------------------

def select_racer(racer_name: str):
    """
    버튼 클릭 시 호출되는 함수: 
    선택된 레이서 이름을 session_state에 저장합니다.
    """
    # 1. 이미 선택된 레이서를 취소하는 로직 (선택적)
    if racer_name == st.session_state['selected_racer1']:
        st.session_state['selected_racer1'] = None
    elif racer_name == st.session_state['selected_racer2']:
        st.session_state['selected_racer2'] = None
        
    # 2. 새 레이서를 선택하는 로직
    elif st.session_state['selected_racer1'] is None:
        st.session_state['selected_racer1'] = racer_name
    elif st.session_state['selected_racer2'] is None:
        st.session_state['selected_racer2'] = racer_name
    else:
        # 두 칸이 모두 차있으면, 첫 번째 레이서를 교체
        st.session_state['selected_racer1'] = racer_name

# ------------------------------------------------------------
# 4. 상단 버튼 구성
# ------------------------------------------------------------

st.markdown("### 1. 비교할 레이서 선택")
button_cols = st.columns(len(driver_name_list) // 4) # 버튼을 두 줄로 배치하기 위해 컬럼 분할

for i, racer in enumerate(driver_name_list):
    # 레이서가 현재 선택 상태인지 확인하여 버튼 스타일 지정
    is_selected_1 = racer == st.session_state['selected_racer1']
    is_selected_2 = racer == st.session_state['selected_racer2']
    
    # 선택된 버튼의 레이블에 표시 추가
    button_label = racer
    if is_selected_1:
        button_label = f"🔴 {racer} (1)"
    elif is_selected_2:
        button_label = f"🔵 {racer} (2)"

    # 버튼을 5개씩 두 줄에 배치
    col_index = i % (len(driver_name_list) // 4)
    
    with button_cols[col_index]:
        # 버튼 클릭 시 select_racer 함수 호출
        if st.button(button_label, key=f"btn_{racer}", use_container_width=True):
            select_racer(racer)

            path_name = racer.lower().replace(" ", "-")
            statisticsDB = StatisticsDBManager()
            stats: Statistic = statisticsDB.select_season_stats_by_driver(path_name)
            career: CareerStatistic = statisticsDB.select_career_stats_by_driver(path_name)

st.markdown("---")

# ------------------------------------------------------------
# 5. 3개 컬럼 레이아웃 구성
# ------------------------------------------------------------

col1, col2 = st.columns([1, 1])

racer1_name = st.session_state['selected_racer1']
racer2_name = st.session_state['selected_racer2']

# ------------------------------------------------
# 5.1. 왼쪽 컬럼: 레이서 1 정보
# ------------------------------------------------
# statisticsDB = StatisticsDBManager()
# stats: Statistic = statisticsDB.select_season_stats_by_driver(data.name)
# career: CareerStatistic = statisticsDB.select_career_stats_by_driver(data.name)


with col1:
    st.subheader("🔴 레이서 1")
    if racer1_name:
        st.metric("선택된 레이서", racer1_name)
        # 레이서 1 상세 정보 (데이터 로딩 필요)
        st.info(f"팀: [DB에서 {racer1_name}의 팀 로딩]")
        st.info(f"국적: [DB에서 {racer1_name}의 국적 로딩]")
    else:
        st.warning("레이서 1을 선택해 주세요.")


# ------------------------------------------------
# 5.2. 오른쪽 컬럼: 레이서 2 정보
# ------------------------------------------------
with col2:
    st.subheader("🔵 레이서 2")
    if racer2_name:
        st.metric("선택된 레이서", racer2_name)
        # 레이서 2 상세 정보 (데이터 로딩 필요)
        st.info(f"팀: [DB에서 {racer2_name}의 팀 로딩]")
        st.info(f"국적: [DB에서 {racer2_name}의 국적 로딩]")
    else:
        st.warning("레이서 2를 선택해 주세요.")


# ------------------------------------------------
# 5.3. 중앙 컬럼: 비교 항목 (두 명 모두 선택되었을 때만 표시)
# ------------------------------------------------
# with col_center:
#     # 두 레이서가 모두 선택되었을 때만 중앙 컬럼 내용을 표시
#     if racer1_name and racer2_name and racer1_name != racer2_name:
#         st.subheader(f"⚖️ {racer1_name} vs {racer2_name} 비교")
#         st.markdown("---")

#         # ------------------------------------------------
#         # A. 누적 포인트 비교
#         # ------------------------------------------------
#         st.metric("🏆 누적 포인트", 
#                   value="[총 포인트 데이터 로딩]", 
#                   delta="[포인트 차이 데이터 로딩]")

#         # st.line_chart(point_comparison_data) # 시즌별 포인트 추이 그래프
#         st.caption("👈 여기에 시즌 누적 포인트 비교 차트가 표시됩니다.")

#         st.markdown("---")

#         # ------------------------------------------------
#         # B. 주요 통계 비교
#         # ------------------------------------------------
#         st.markdown("**주요 통계 기록**")
        
#         stat_col1, stat_col2 = st.columns(2)
        
#         with stat_col1:
#             st.text(f"🥇 우승 (R1): [우승 횟수 로딩]")
#             st.text(f"🏁 폴 포지션 (R1): [폴 포지션 로딩]")
        
#         with stat_col2:
#             st.text(f"🥇 우승 (R2): [우승 횟수 로딩]")
#             st.text(f"🏁 폴 포지션 (R2): [폴 포지션 로딩]")

#     elif racer1_name and racer2_name and racer1_name == racer2_name:
#         st.warning("같은 레이서를 두 번 선택했습니다. 다른 레이서를 선택해 주세요.")
#     else:
#         st.info("두 레이서를 모두 선택하면 비교 분석 결과가 여기에 표시됩니다.")
