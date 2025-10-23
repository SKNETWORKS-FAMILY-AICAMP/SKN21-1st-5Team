/*
 * DB 는 localDB 사용
 * 
 * 작성자: 신병탁
 * 날짜: 2025-10-23
 */

CREATE DATABASE 1st_pjt;
USE  1st_pjt;

DROP TABLE IF EXISTS  drivers;
DROP TABLE IF EXISTS country;
CREATE TABLE country (
	country_id VARCHAR(10) PRIMARY key COMMENT '나라 코드',
  	country_name VARCHAR(50) NOT NULL UNIQUE COMMENT '나라이름',
	description VARCHAR(500) COMMENT '설명',
  	create_date DATE NOT NULL COMMENT '생성일시'
) COMMENT='나라 정보';

DROP TABLE IF EXISTS team;
CREATE TABLE team (
	team_id INT PRIMARY key AUTO_INCREMENT COMMENT '팀 아이디',
  	team_name VARCHAR(50) NOT NULL UNIQUE COMMENT '팀이름',
  	establish int COMMENT '설립년도',
  	chief VARCHAR(50) COMMENT '대표',
  	description VARCHAR(500) COMMENT '설명',
  	create_date DATE NOT NULL COMMENT '생성일시'
) COMMENT='팀 정보';

DROP TABLE IF EXISTS  drivers;
CREATE table drivers (
	driver_id INT PRIMARY key AUTO_INCREMENT COMMENT '아이디',
  	name VARCHAR(50) NOT NULL COMMENT '이름',
  	team_id INT COMMENT '팀 아이디',
  	country_id VARCHAR(10)   NOT NULL COMMENT '나라 아이디',
  	email varchar(100) unique key COMMENT '이메일',
  	gender char(1) check(gender in('m', 'f')) COMMENT '성별(m,f)',
  	description VARCHAR(500) COMMENT '설명',
  	image_url text NULL DEFAULT NULL COMMENT '이미지',
  	create_date DATE NOT NULL COMMENT '생성일시',
	CONSTRAINT fk_team FOREIGN KEY(team_id) REFERENCES team(team_id),
    CONSTRAINT fk_country FOREIGN KEY(country_id) REFERENCES country(country_id)
) COMMENT='드라이버 정보';