def azureml_main(frame1):
  import pandas as pd
  import os.path

## Filter out outliers 
  frame1 = frame1[(frame1["FFMC"] > 40.0) & \
                                (frame1["ISI"] < 30.0) & \
                                (frame1["rain"] < 3.0)]
  return frame1
