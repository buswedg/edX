gps = LOAD '/data/racecar/source/gps.avro' USING AvroStorage();
gpsfilt = FILTER gps BY (Position IS NOT NULL) AND (Time IS NOT NULL);
gpstable = FOREACH gpsfilt GENERATE Time, FLATTEN(Position), Speed;
STORE gpstable INTO '/data/racecar/gps';

eng = LOAD '/data/racecar/source/engine.avro' USING AvroStorage();
engtable = FILTER eng BY (OilTemp IS NOT NULL) AND (Revs IS NOT NULL);
STORE engtable INTO '/data/racecar/engine';

brk = LOAD '/data/racecar/source/brake.avro' USING AvroStorage();
brktable = FILTER brk BY BrakeTemp IS NOT NULL;
STORE brktable INTO '/data/racecar/brake';