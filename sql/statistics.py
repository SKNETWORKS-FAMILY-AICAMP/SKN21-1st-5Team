'''
작성자: 김가람
날짜: 2025-10-23
'''
import pymysql
from sql import drivers
from datetime import datetime
from data.connect import WebConnectManager

db_host = "127.0.0.1"
db_port = 3306
# user_name = "lucy"
user_name = "playdata"
db_password = "1111"
db_name = "1st_pjt"

def insert_season_statistics():
    driver_list = drivers.select_drivers()
    for d in driver_list:
        name = d[0]
        path_name = name.lower().replace(" ", "-")
        print(path_name)

def insert_statistics():
    pass
