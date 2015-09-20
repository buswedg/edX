set hive.execution.engine=tez;

DROP VIEW IF EXISTS lap;
DROP TABLE IF EXISTS gps;
DROP TABLE IF EXISTS engine;
DROP TABLE IF EXISTS brake;

CREATE EXTERNAL TABLE gps
(laptime STRING,
 lat DOUBLE,
 lon DOUBLE,
 speed FLOAT)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE LOCATION '/data/racecar/gps';

CREATE EXTERNAL TABLE engine
(laptime STRING,
 revs FLOAT,
 oiltemp FLOAT)
 ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
 STORED AS TEXTFILE LOCATION '/data/racecar/engine';

CREATE EXTERNAL TABLE brake
(laptime STRING,
 braketemp FLOAT)
 ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
 STORED AS TEXTFILE LOCATION '/data/racecar/brake';

CREATE VIEW lap
AS
SELECT gps.*, engine.revs, engine.oiltemp, brake.braketemp
FROM gps LEFT OUTER JOIN engine ON (gps.laptime = engine.laptime)
LEFT OUTER JOIN brake ON (gps.laptime = brake.laptime);