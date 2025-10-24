/*
 * DB 는 localDB 사용
 */

-- CREATE DATABASE 1st_pjt;
USE  1st_pjt;

DROP TABLE IF EXISTS  country;
DROP TABLE IF EXISTS  drivers_2;
DROP TABLE IF EXISTS  team;

DROP TABLE IF EXISTS  drivers;
CREATE table drivers (
 	name VARCHAR(50) PRIMARY key COMMENT '이름',
  	team_id VARCHAR(50) COMMENT '팀 아이디',
  	country_id VARCHAR(50)   NOT NULL COMMENT '나라 아이디',
  	email varchar(100) unique key COMMENT '이메일',
  	gender char(1) check(gender in('m', 'f')) COMMENT '성별(m,f)',
  	description VARCHAR(500) COMMENT '설명',
  	image_url text NULL DEFAULT NULL COMMENT '이미지',
  	create_date DATETIME NOT NULL COMMENT '생성일시'
) COMMENT='드라이버 정보';

DROP TABLE IF EXISTS  season_stats;
CREATE TABLE season_stats (
	name VARCHAR(50) PRIMARY key COMMENT '이름',
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
) COMMENT='선수별 시즌성적';

DROP TABLE IF EXISTS  career_stats;
CREATE TABLE career_stats (
	name VARCHAR(50) PRIMARY key COMMENT '이름',
	year int NULL,
	grand_prix_entered int,
  	career_points int,
	highest_race_finish int,
	podiums int,
	highest_grid_position int,
	pole_positions int,
	world_championships int,
	dnfs int,
  	create_date DATETIME NOT NULL COMMENT '생성일시'
) COMMENT='선수별 통산성적';


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