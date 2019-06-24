import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.linear_model import LinearRegression
from statistics import mean


weather = pd.read_csv('weatherHistory.csv')
weather[weather['Precip Type'].isnull()]


