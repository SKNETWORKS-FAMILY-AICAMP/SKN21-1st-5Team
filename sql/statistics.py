'''
작성자: 김가람
날짜: 2025-10-23
'''
import pymysql
from datetime import datetime
from data.connect import WebConnectManager
from data.driver import Statistic
from data.driver import CareerStatistic
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
                print(keys)
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

    def insert_career_stats_aggr(self):
        try:
            conn = None
            cursor = None

            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                insert_sql = """
                            INSERT INTO career_stats_aggr (grand_prix_entered,career_points,highest_race_finish,podiums,highest_grid_position,pole_positions,world_championships,dnfs,create_date)
                            select 
                            avg(nullif(grand_prix_entered, 0))          as grand_prix_entered      
                            , avg(nullif(career_points, 0))             as career_points           
                            , avg(nullif(highest_race_finish, 0))       as highest_race_finish     
                            , avg(nullif(podiums, 0))                   as podiums                 
                            , avg(nullif(highest_grid_position, 0))     as highest_grid_position   
                            , avg(nullif(pole_positions, 0))            as pole_positions          
                            , avg(nullif(world_championships, 0))       as world_championships     
                            , avg(nullif(dnfs, 0))		                as dnfs    
                            , max(now())                            	as create_date             
                            from career_stats
                           """              
                with conn.cursor() as cursor:
                        result = cursor.execute(insert_sql)
                        conn.commit()
                        print("처리 행수:", result)
                    # return result
        finally:
            pass
        
    def merge_season_stats_aggr(self):
        try:
            conn = None
            cursor = None

            with pymysql.connect(host=self.db_host, port=self.db_port, user=self.user_name, password=self.db_password, db=self.db_name) as conn:
                merge_sql = """
                           INSERT INTO season_stats_aggr (
                                year
                                , season_position
                                , season_points
                                , grand_prix_races
                                , grand_prix_points
                                , grand_prix_wins
                                , grand_prix_podiums
                                , grand_prix_poles
                                , grand_prix_top_10s
                                , dhl_fastest_laps
                                , dnfs
                                , sprint_races
                                , sprint_points
                                , sprint_wins
                                , sprint_podiums
                                , sprint_poles
                                , sprint_top_10s
                                , create_date	
                            )
                            select 
                                year(now())								as year 
                                , avg(nullif(season_position, 0))       as season_position	
                                , avg(nullif(season_points, 0))         as season_points      
                                , avg(nullif(grand_prix_races, 0))      as grand_prix_races   
                                , avg(nullif(grand_prix_points, 0))     as grand_prix_points  
                                , avg(nullif(grand_prix_wins, 0))       as grand_prix_wins    
                                , avg(nullif(grand_prix_podiums, 0))    as grand_prix_podiums 
                                , avg(nullif(grand_prix_poles, 0))      as grand_prix_poles   
                                , avg(nullif(grand_prix_top_10s, 0))    as grand_prix_top_10s 
                                , avg(nullif(dhl_fastest_laps, 0))      as dhl_fastest_laps   
                                , avg(nullif(dnfs, 0))                  as dnfs               
                                , avg(nullif(sprint_races, 0))          as sprint_races       
                                , avg(nullif(sprint_points, 0))         as sprint_points      
                                , avg(nullif(sprint_wins, 0))           as sprint_wins        
                                , avg(nullif(sprint_podiums, 0))        as sprint_podiums     
                                , avg(nullif(sprint_poles, 0))          as sprint_poles       
                                , avg(nullif(sprint_top_10s, 0))        as sprint_top_10s     
                                , max(now())                            as create_date 
                            from season_stats
                            ON DUPLICATE KEY UPDATE
                                season_position		= season_position	
                                , season_points         = season_points      
                                , grand_prix_races      = grand_prix_races   
                                , grand_prix_points     = grand_prix_points  
                                , grand_prix_wins       = grand_prix_wins    
                                , grand_prix_podiums    = grand_prix_podiums 
                                , grand_prix_poles      = grand_prix_poles   
                                , grand_prix_top_10s    = grand_prix_top_10s 
                                , dhl_fastest_laps      = dhl_fastest_laps   
                                , dnfs                  = dnfs               
                                , sprint_races          = sprint_races       
                                , sprint_points         = sprint_points      
                                , sprint_wins           = sprint_wins        
                                , sprint_podiums        = sprint_podiums     
                                , sprint_poles          = sprint_poles       
                                , sprint_top_10s        = sprint_top_10s   
                                , create_date			= create_date
                           """              
                with conn.cursor() as cursor:
                        result = cursor.execute(merge_sql)
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
        
    def select_season_stats_by_driver(self, name) -> Statistic:
        # 특정 레이서 시즌 성적 조회
        result = self._select_connect(f"select name, season_position, season_points, grand_prix_races, grand_prix_points, grand_prix_wins, grand_prix_podiums, grand_prix_poles, grand_prix_top_10s, dhl_fastest_laps, dnfs, sprint_races, sprint_points, sprint_wins, sprint_podiums, sprint_poles, sprint_top_10s from season_stats where name = '{name}'").fetchone()
        return Statistic(*result)
        
    def select_career_statistics(self) -> list:
        # 레이서 선수 성적 전체 조회
        result = self._select_connect('select * from career_stats').fetchall()

        if result:
            datas = []

            for r in result:
                datas.append(r)
                
            return datas
        else:
            return []
        
    def select_season_stats_aggr(self) -> dict:
        # 시즌별성적 집계(평균값)
        insert_sql = """
                select
                    year
                    , season_position
                    , season_points
                    , grand_prix_races
                    , grand_prix_points
                    , grand_prix_wins
                    , grand_prix_podiums
                    , grand_prix_poles
                    , grand_prix_top_10s
                    , dhl_fastest_laps
                    , dnfs
                    , sprint_races
                    , sprint_points
                    , sprint_wins
                    , sprint_podiums
                    , sprint_poles
                    , sprint_top_10s
                    , create_date
                from season_stats_aggr
                """
        result = self._select_connect_dict(insert_sql).fetchone()
        print(result)

    def selectcareer_stats_aggr(self) -> dict:
        # 통산성적 집계(평균값)
        result = self._select_connect_dict(f"select grand_prix_entered,career_points,highest_race_finish,podiums,highest_grid_position,pole_positions,world_championships,dnfs,create_date from career_stats_aggr").fetchone()
        print(result)

    def select_career_stats_by_driver(self, name) -> CareerStatistic:
        # 특정 레이서 성적 조회
        result = self._select_connect(f"select name, grand_prix_entered, career_points, highest_race_finish, podiums, highest_grid_position, pole_positions, world_championships, dnfs from career_stats where name = '{name}'").fetchone()
        return CareerStatistic(*result)
