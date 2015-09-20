@outputSchema("f_readings: {(year:chararray, month:int, maxtemp:float, mintemp:float, frostdays:int, rainfall:float, sunshinehours:chararray)}")
def fahrenheit(c_reading):
  year, month, maxtemp, mintemp, frostdays, rainfall, sunshine = c_reading.split(' ')
  maxtemp_f = float(maxtemp) * 9/5 + 32
  mintemp_f = float(mintemp) * 9/5 + 32
  return year, int(month), maxtemp_f, mintemp_f, frostdays, float(rainfall), sunshine

