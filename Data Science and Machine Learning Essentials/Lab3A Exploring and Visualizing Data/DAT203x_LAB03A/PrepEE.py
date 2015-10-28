
## Load the data  
import pandas as pd
import os
from sklearn import preprocessing

pathName = "c://DAT203xLabfiles"
fileName = "EnergyEfficiencyRegressiondata.csv"
filePath = os.path.join(pathName, fileName)
eeframe = pd.read_csv(filePath)

## Remove columns we're not going to use
eeframe = eeframe.drop('Cooling Load', 1)  

## scale numeric features
scaleList = ["Relative Compactness", "Surface Area", \
       "Wall Area", "Roof Area", "Glazing Area",  \
       "Glazing Area Distribution"]
arry = eeframe[scaleList].as_matrix()
eeframe[scaleList] = preprocessing.scale(arry)  
        
