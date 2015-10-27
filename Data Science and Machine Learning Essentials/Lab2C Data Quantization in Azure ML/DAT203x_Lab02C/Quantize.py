def azureml_main(frame1):
## Quantize the wind into 4 categories using cut with explicit columns.
  import pandas as pd
  bins = [0, 2.5, 5, 7.5, 10] 
  frame1['wind_cat'] = pd.cut(frame1['wind'], bins)
  return frame1
