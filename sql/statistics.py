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
        wm = WebConnectManager()
        print(wm.get_driver(path_name))

def insert_statistics():
    driver_list = drivers.select_drivers()
    for d in driver_list:
        name = d[0]
        path_name = name.lower().replace(" ", "-")
        print(path_name)
        wm = WebConnectManager()
        print(wm.get_driver_career(path_name))

def select_statistics():
    # sql = 'select * from drivers'
    # with pymysql.connect(host=db_host, port=db_port, user=user_name, password=db_password, db=db_name) as conn:
    #     with conn.cursor() as cursor:
    #         result = cursor.execute(sql)
    #         print("처리 행수:", result)
            
    #         return cursor.fetchall()