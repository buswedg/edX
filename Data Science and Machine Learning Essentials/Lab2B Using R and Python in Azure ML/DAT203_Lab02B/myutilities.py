def round2(df):
## Round values to 2 decimal places
  import numpy as np
  return df.apply(lambda x: np.round(x, 2))

