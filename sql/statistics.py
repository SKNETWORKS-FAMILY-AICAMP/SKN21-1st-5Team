'''
작성자: 김가람
날짜: 2025-10-23
'''
import pymysql
from datetime import datetime
from data.connect import WebConnectManager
from db_connect import DBManager
from drivers import DriversDBManager

class StatisticsDBManager(DBManager):
    def __init__(self):
        self.driversDB = DriversDBManager()

    def insert_season_statistics(self):
        driver_list = self.driversDB.select_drivers()
        for d in driver_list:
            name = d[0]
            path_name = name.lower().replace(" ", "-")
            wm = WebConnectManager()
            print(wm.get_driver(path_name))

    def insert_statistics(self):
        driver_list = self.driversDB.select_drivers()
        for d in driver_list:
            name = d[0]
            path_name = name.lower().replace(" ", "-")
            wm = WebConnectManager()
            print(wm.get_driver_career(path_name))

    # def select_statistics():
    #     sql = 'select * from drivers'
        
        # with pymysql.connect(host=db_host, port=db_port, user=user_name, password=db_password, db=db_name) as conn:
        #     with conn.cursor() as cursor:
        #         result = cursor.execute(sql)
        #         print("처리 행수:", result)
                
        #         return cursor.fetchall()