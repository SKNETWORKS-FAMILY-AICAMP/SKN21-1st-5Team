'''
작성자: 김가람
날짜: 2025-10-22
'''
import pymysql
from datetime import datetime
from data.connect import WebConnectManager
from sql.db_connect import DBManager

class DriversDBManager(DBManager):
    def __init__(self):
        self.wm = WebConnectManager()

    # drivers_db.py
    def insert_team(self):
        pass

    def insert_country(self, name, email, tall, birthday):
        pass

    def insert_driver(self):

        self.delete_driver_all()
        
        try:
            conn = None
            cursor = None
            # print(wm.get_drivers2())
            # insert_sql = "insert into drivers (name, team_id, country_id, email, gender, description, image_url, create_date) values(%s, %s, %s, %s, %s)"
            insert_sql = 'insert into drivers (name, team_id, country_id, image_url, create_date) values (%s, %s, %s, %s, %s)'
            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                for v in self.wm.get_drivers():
                    with conn.cursor() as cursor:
                        name = v['name']
                        team = v['team']
                        country = v['country'].replace('Flag of ', '')
                        image_url = v['image_url']
                        create_date = datetime.now()

                        print(f'name : {name},  {team}, {country}, {image_url}, {create_date}')

                        result = cursor.execute(insert_sql, [name, team, country, image_url, create_date])
                        conn.commit()
                        print("처리 행수:", result)
                        # return result
        finally:
            pass

    def update_team(self, team_id):
        pass
    def update_country(self, ountry_id):
        pass
    def update_driver(self, driver_id):
        pass

    def delee_team(self, team_id):
        pass
    def delete_country(self, country_id):
        pass

    def delete_driver_all(self):
        try:
            conn = None
            cursor = None
            delete_sql = 'delete from drivers'
            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                cursor = conn.cursor()

                for v in self.wm.get_drivers():
                    with conn.cursor() as cursor:
                        result = cursor.execute(delete_sql)
                        conn.commit()
                        print("처리 행수:", result)
        finally:
            pass

    def select_country(self):
        pass # 전체조회

    def select_teams(self):
        return self.select_connect('select distinct team_id from drivers').fetchall()

    def select_drivers(self):
        # 드라이버 리스트 전체 조회
        return self.select_connect('select * from drivers').fetchall()

    def select_drivers_by_team(self, team_id: str):
        # 드라이버 리스트 팀 분류 - 전체 조회
        print(f"select * from drivers where team_id = '{team_id}'")
        return self.select_connect(f"select * from drivers where team_id = '{team_id}'").fetchall()

    def select_driver_by_keyword(self, keyword):
        sql = f"select * from drivers where name LIKE '%{keyword}%'"
        return self.select_connect(sql).fetchall()

    def select_driver_by_id(driver_id):
        pass # ID로 조회

dbmanager = DriversDBManager()
