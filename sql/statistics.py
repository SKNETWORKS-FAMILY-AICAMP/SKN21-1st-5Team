'''
작성자: 김가람
날짜: 2025-10-23
'''
import pymysql
from datetime import datetime
from data.connect import WebConnectManager
from data.driver import Statistic
from sql.db_connect import DBManager
from sql.drivers import DriversDBManager

class StatisticsDBManager(DBManager):
    def __init__(self):
        self.wm = WebConnectManager()
        self.driversDB = DriversDBManager()

    def insert_driver_statistics(self):
        self.delete_statistics_all()

        driver_list = self.driversDB.select_drivers()

        for d in driver_list:
            self._insert_season_statistics(d.name)
            self._insert_statistics(d.name)

    def _insert_season_statistics(self, name):        
        try:
            conn = None
            cursor = None
            
            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                dict = self.wm.get_driver(name)
                dict["create_date"] = datetime.now()

                keys = tuple(dict.keys())
                insert_sql = 'insert into season_stats ' + str(keys).replace("'", "") + ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                
                # dict 순서 보장이 안되므로, key 값과 value 값 순서 맞추기 위한 values.
                values = []
                for k in keys:
                    values.append(dict[k])

                with conn.cursor() as cursor:
                    result = cursor.execute(insert_sql, values)
                    conn.commit()
                    print("처리 행수:", result)
                    # return result
        finally:
            pass


    def _insert_statistics(self, name):
        try:
            conn = None
            cursor = None

            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                dict = self.wm.get_driver_career(name)
                dict["create_date"] = datetime.now()

                keys = tuple(dict.keys())
                insert_sql = 'insert into career_stats ' + str(keys).replace("'", "") + ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

                # dict 순서 보장이 안되므로, key 값과 value 값 순서 맞추기 위한 values.
                values = []
                for k in keys:
                    values.append(dict[k])

                with conn.cursor() as cursor:
                    result = cursor.execute(insert_sql, values)
                    conn.commit()
                    print("처리 행수:", result)
                    # return result

        finally:
            pass

    def delete_statistics_all(self):
        self._delete_season_statistics()
        self._delete_career_statistics()

    def _delete_season_statistics(self):
        self._delete_connect('delete from season_stats')

    def _delete_career_statistics(self):
        self._delete_connect('delete from career_stats')

    def select_season_statistics(self) -> list:
        # 시즌 성적 전체 조회
        result = self._select_connect('select * from season_stats').fetchall()

        if result:
            datas = []

            for r in result:
                datas.append(r)
                
            return datas
        else:
            return []
        
    def select_career_statistics(self) -> list:
        # 시즌 성적 전체 조회
        result = self._select_connect('select * from career_stats').fetchall()

        if result:
            datas = []

            for r in result:
                datas.append(r)
                
            return datas
        else:
            return []

