-- Load the weather source data
Source = LOAD '/data/weather' USING PigStorage('\t') AS (year:chararray, month:int, maxtemp:float, mintemp:float, frostdays:int, rainfall:float, sunshinehours:chararray);

-- filter the data to remove notes and header row
Data = FILTER Source BY maxtemp IS NOT NULL AND mintemp IS NOT NULL AND year != 'yyyy';

-- Delete missing values symbol (---)
DataVals = FOREACH Data GENERATE year, month, maxtemp, mintemp, frostdays, rainfall, REPLACE(sunshinehours, '---', '') AS sunshinehours;

-- Split into clean and dirty readings based on presence of a sunshine sensor symbol (#)
CleanReadings = FILTER DataVals BY INDEXOF(sunshinehours, '#', 0) <= 0;
DirtyReadings = FILTER DataVals BY INDEXOF(sunshinehours, '#', 0) > 0;

-- Clean the dirty readings to remove # symbol for sunshine sensor
CleanedReadings = FOREACH DirtyReadings GENERATE year, month, maxtemp, mintemp, frostdays, rainfall, SUBSTRING(sunshinehours, 0, INDEXOF(sunshinehours, '#', 0)) AS sunshinehours;

-- Combine the clean and cleaned readings
Readings = UNION CleanReadings, CleanedReadings;

-- Sort Readings
SortedReadings = ORDER Readings BY year ASC, month ASC;

-- Save the scrubbed data
STORE SortedReadings INTO '/data/scrubbedweather';