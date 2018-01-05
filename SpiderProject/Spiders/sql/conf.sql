-- 是否为整租的枚举类
CREATE TYPE entire_type AS ENUM ('0','1');
-- 房屋结构体
CREATE TABLE house(
  id SERIAL PRIMARY KEY,
  title VARCHAR(50) NOT NULL ,
  house_link text NOT NULL ,
  hash_link VARCHAR(32) NOT NULL ,
  meters FLOAT NOT NULL ,
  bedroom INT,
  living_room INT,
  toilet INT,
  people_sum INT DEFAULT 0,
  source VARCHAR(10) NOT NULL ,
  rent_way int NOT NULL ,
  city_code INT NOT NULL REFERENCES city(city_code),
  region_lo VARCHAR(50) NOT NULL ,
  region_hi VARCHAR(50) NOT NULL ,
  subway INT NOT NULL ,
  price INT NOT NULL ,
  detail VARCHAR(50),
  village VARCHAR(20)
);
-- 创建索引
CREATE INDEX ON house(region_hi);
CREATE INDEX ON house(village);
CREATE UNIQUE INDEX ON house(hash_link);
-- 插入数据
INSERT INTO house (title, house_link, hash_link, meters, bedroom, living_room, toilet, people_sum, source, rent_way, city_code, region_lo, region_hi, subway, price, detail, village)
VALUES ();
-- 删除表
DROP TABLE house;
SELECT count(*)
FROM house;

-- 检测表
SELECT tablename
FROM
  pg_tables
WHERE tablename='house';

SELECT count(*)
FROM house
WHERE source!='lj';
SELECT *
FROM house;
-- 清空表数据
DELETE FROM house
WHERE source='lj';

-- 城市信息
CREATE TABLE city(
  id SERIAL PRIMARY KEY ,
  province_name VARCHAR(20) NOT NULL ,
  city_name VARCHAR(20) NOT NULL ,
  city_code INT
);
CREATE INDEX ON city(city_name);
CREATE UNIQUE INDEX ON city(city_code);
INSERT INTO city (province_name, city_name, city_code) VALUES ();


CREATE TABLE region(
  id SERIAL PRIMARY KEY ,
  region_name VARCHAR(20),
  city_code INT REFERENCES city(city_code)
);

