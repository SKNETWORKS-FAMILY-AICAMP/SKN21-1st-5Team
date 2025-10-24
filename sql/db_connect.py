'''
작성자: 김가람
날짜: 2025-10-23
'''
import pymysql

class DBManager:
    db_host = "127.0.0.1"
    db_port = 3306
    # user_name = "lucy"
    user_name = "playdata"
    db_password = "1111"
    db_name = "1st_pjt"
    
    def _select_connect(self, sql):
        try:
            conn = None
            cursor = None
            
            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    return cursor
        finally:
            pass
            
    def _delete_connect(self, sql):
        try:
            conn = None
            cursor = None

            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                cursor = conn.cursor()

                with conn.cursor() as cursor:
                    result = cursor.execute(sql)
                    conn.commit()
        finally:
            pass

