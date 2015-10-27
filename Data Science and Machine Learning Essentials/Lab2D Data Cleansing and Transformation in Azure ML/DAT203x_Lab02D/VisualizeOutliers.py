def azureml_main(frame1):
  import matplotlib
  matplotlib.use('agg')
  
  import pandas as pd
  import matplotlib.pyplot as plt
  from pandas.tools.plotting import scatter_matrix 

## Remove unwanted columns 
  frame1.drop(["X", "Y", "month", "day"], axis = 1, inplace = True)

## Create a scatter plot matrix 
  fig1 = plt.figure(1, figsize = (12,9))
  ax = fig1.gca()
  scatter_matrix(frame1, alpha=0.2, figsize=(10, 10), diagonal='kde', ax=ax)
  fig1.savefig('scatter2.png')
  return frame1
