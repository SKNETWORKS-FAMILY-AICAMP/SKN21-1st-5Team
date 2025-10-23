'''
작성자: 김가람
날짜: 2025-10-22
'''
import pymysql
from datetime import datetime
from data.connect import WebConnectManager

db_host = "127.0.0.1"
db_port = 3306
user_name = "lucy"
db_password = "1111"
db_name = "1st_pjt"

# drivers_db.py
def insert_team():
    pass

def insert_country(name, email, tall, birthday):
    pass

def insert_driver():

    delete_driver_all()
    
    try:
        conn = None
        cursor = None
        wm = WebConnectManager()
        # print(wm.get_drivers2())
        # insert_sql = "insert into drivers (name, team_id, country_id, email, gender, description, image_url, create_date) values(%s, %s, %s, %s, %s)"
        insert_sql = 'insert into drivers (name, team_id, country_id, image_url, create_date) values (%s, %s, %s, %s)'
        with pymysql.connect(host=db_host, port=db_port, user=user_name, password=db_password, db=db_name) as conn:
            for v in wm.get_drivers():
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

def delete_driver_all():
    try:
        conn = None
        cursor = None
        wm = WebConnectManager()
        delete_sql = 'delete from drivers'
        with pymysql.connect(host="127.0.0.1", port=3306, user='playdata', password='1111', db='1st_pjt') as conn:
            cursor = conn.cursor()

            for v in wm.get_drivers():
                with conn.cursor() as cursor:
                    result = cursor.execute(delete_sql)
                    conn.commit()
                    print("처리 행수:", result)
    finally:
        pass


def select_team():
    print('have a good')
    WebConnectManager().get_drivers()
    pass # 전체조회
def select_country():
    pass # 전체조회

def select_drivers():
    # 드라이버 리스트 전체 조회
    sql = 'select * from drivers'
    with pymysql.connect(host=db_host, port=db_port, user=user_name, password=db_password, db=db_name) as conn:
        with conn.cursor() as cursor:
                result = cursor.execute(sql)
                print("처리 행수:", result)

def select_driver():
    pass

def select_driver_by_keyword(keyword):
    sql = f"select * from drivers where name LIKE '%{keyword}%'"

    with pymysql.connect(host=db_host, port=db_port, user=user_name, password=db_password, db=db_name) as conn:
        with conn.cursor() as cursor:
                result = cursor.execute(sql)
                print("처리 행수:", result)

def select_driver_by_id(driver_id):
    pass # ID로 조회
