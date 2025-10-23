'''
작성자: 김가람
날짜: 2025-10-22
'''
import pymysql
from data.connect import WebConnectManager
from datetime import datetime

# drivers_db.py
def insert_team():
    try:
        conn = None
        cursor = None
        wm = WebConnectManager()
        # print(wm.get_drivers2())
        # insert_sql = "insert into drivers (name, team_id, country_id, email, gender, description, image_url, create_date) values(%s, %s, %s, %s, %s)"
        insert_sql = 'insert into drivers (name, team_id, country_id, create_date) values (%s, %s, %s, %s)'
        with pymysql.connect(host="127.0.0.1", port=3306, user='playdata', password='1111', db='1st_pjt') as conn:
            for v in wm.get_drivers_dict():
                with conn.cursor() as cursor:
                    name = v['name']
                    team = v['team']
                    country = v['country'].replace('Flag of ', '')
                    create_date = datetime.now()

                    print(f'name : {name},  {team}, {country}, {create_date}')

                    result = cursor.execute(insert_sql, [name, team, country, create_date])
                    conn.commit()
                    print("처리 행수:", result)
    finally:
        pass

def insert_country(name, email, tall, birthday):
    pass
def insert_driver(name, team, country, img):
    pass

def update_team(team_id):
    pass
def update_country(country_id):
    pass
def update_driver(driver_id):
    pass

def delee_team(team_id):
    pass
def delete_country(country_id):
    pass
def delete_driver(driver_id):
    pass


def select_team():
    pass # 전체조회
def select_country():
    pass # 전체조회
def select_driver():
    pass # 전체조회
def select_driver_by_id(driver_id):
    pass # ID로 조회

insert_team()
