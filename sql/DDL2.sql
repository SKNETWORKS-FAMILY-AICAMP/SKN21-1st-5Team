USE  1st_pjt;

-- 재 실행 시 에러발생함
ALTER TABLE career_stats ADD year INT NULL AFTER name;

DROP TABLE IF EXISTS  season_stats_aggr;
CREATE TABLE season_stats_aggr (
	year int PRIMARY key COMMENT '년도',
	season_position int,
  	season_points int,
	grand_prix_races int,
	grand_prix_points int,
	grand_prix_wins int,
	grand_prix_podiums int,
	grand_prix_poles int,
	grand_prix_top_10s int,
	dhl_fastest_laps int,
	dnfs int,
	sprint_races int,
	sprint_points int,
	sprint_wins int,
	sprint_podiums int,
	sprint_poles int,
	sprint_top_10s int,
  	create_date DATETIME NOT NULL COMMENT '생성일시'
) COMMENT='시즌별성적 집계';

DROP TABLE IF EXISTS  career_stats_aggr;
CREATE TABLE career_stats_aggr (
	id int PRIMARY key AUTO_INCREMENT COMMENT '아이디',
	grand_prix_entered int,
  	career_points int,
	highest_race_finish int,
	podiums int,
	highest_grid_position int,
	pole_positions int,
	world_championships int,
	dnfs int,
  	create_date DATETIME NOT NULL COMMENT '생성일시'
) COMMENT='통산성적 집계';

-- season_stats 초기데이터
INSERT INTO season_stats (name,season_position,season_points,grand_prix_races,grand_prix_points,grand_prix_wins,grand_prix_podiums,grand_prix_poles,grand_prix_top_10s,dhl_fastest_laps,dnfs,sprint_races,sprint_points,sprint_wins,sprint_podiums,sprint_poles,sprint_top_10s,create_date) VALUES
	 ('Alexander Albon',8,73,19,70,0,0,0,11,0,3,4,3,0,0,0,1,'2025-10-24 06:27:32'),
	 ('Carlos Sainz',5,45,12,85,6,8,9,11,7,3,4,3,8,6,8,3,'2025-10-24 06:27:32'),
	 ('Charles Leclerc',6,4,8,45,5,9,5,8,9,2,5,8,7,3,5,2,'2025-10-24 06:27:32');

-- career_stats 초기데이터
INSERT INTO career_stats (name,`year`,grand_prix_entered,career_points,highest_race_finish,podiums,highest_grid_position,pole_positions,world_championships,create_date) VALUES
	 ('Alexander Albon',2025,7,1366,1,15,1,5,4,'2025-10-24 06:27:32'),
	 ('Carlos Sainz',2025,117,1367,1,0,1,5,6,'2025-10-24 06:27:32'),
	 ('Charles Leclercn',2025,17,4366,1,15,1,0,4,'2025-10-24 06:27:32')
	 ;	 

-- season_stats 평균값 생성
INSERT INTO season_stats_aggr 
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
	;	 

-- career_stats 평균값 생성
INSERT INTO career_stats_aggr (grand_prix_entered,career_points,highest_race_finish,podiums,highest_grid_position,pole_positions,world_championships,dnfs,create_date)
select 
  avg(nullif(grand_prix_entered, 0))        as grand_prix_entered      
, avg(nullif(career_points, 0))             as career_points           
, avg(nullif(highest_race_finish, 0))       as highest_race_finish     
, avg(nullif(podiums, 0))                   as podiums                 
, avg(nullif(highest_grid_position, 0))     as highest_grid_position   
, avg(nullif(pole_positions, 0))            as pole_positions          
, avg(nullif(world_championships, 0))       as world_championships     
, null       								as dnfs    
, max(now())                            	as create_date             
from career_stats
	;	