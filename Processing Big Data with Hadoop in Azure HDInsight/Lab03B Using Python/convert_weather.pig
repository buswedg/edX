REGISTER 'wasb:///data/convert_temp.py' using jython as convert_temp;

-- Load the weather source data
Source = LOAD '/data/scrubbedweather' AS (celsius_readings:chararray);

-- use the UDF to structure and convert the data
ConvertedReadings = FOREACH Source GENERATE convert_temp.fahrenheit(celsius_readings);

-- Save the results
STORE ConvertedReadings INTO '/data/convertedweather';



