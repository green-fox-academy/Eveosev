import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime

%matplotlib inline
LA = pd.read_csv('metro-bike-share-trip-data.csv', index_col=0)
LA = LA.rename(columns = lambda x: x.replace(' ','_').lower())


LA.start_time = LA.start_time.apply(lambda x: pd.to_datetime(x))
LA.end_time = LA.end_time.apply(lambda x: pd.to_datetime(x))



metadata = pd.read_json('socrata_metadata.json', orient = 'split')
LA.head()
LA.info()

#This dataset contains the data in 2016 and 2017
#It is important to do a total statistic to check the total trend.
#It is necessary to separate the data into two sub dataset:
#                        LA_2016 and LA_2017




#Data manipulation


#Passholder type stat 
"""
In this case, 
"""
P_T = LA.groupby('passholder_type').count().reset_index()[['passholder_type', 'duration']]
P_T = P_T.rename(columns = {'duration': 'amount'})
passholder_type = np.array(P_T.passholder_type)
amount = np.array(P_T.amount)
fig1, ax1 = plt.subplots()
ax1.bar(passholder_type, amount)
plt.show()
