import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.linear_model import LinearRegression
from statistics import mean
import inspect


# clf = LinearRegression()
# clf.fit(exes, eyes)


# clf.predict(new_ex)

#Data manipulation & EDA
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
train.columns.tolist()

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    names = [var_name for var_name, var_val in callers_local_vars if var_val is var]
    if len(names) > 0:
        return names[0]

train.corr().abs().unstack()
train['Relatives'] = train.SibSp + train.Parch
train.drop(columns = ['SibSp', 'Parch'])
test.loc[test.Fare.isna(), 'Fare'] = 9

#Survive against Gender
df1 = train.groupby(['Sex', 'Survived']).count().PassengerId
female = [81, 233]
male = [468, 109]
# df = pd.DataFrame({'Female': female, 'Male': male})
# df.plot.bar()
fig, ax = plt.subplots()
n = np.arange(2)
width = 0.35
ax.bar(n, female, width, label = 'Female')
ax.bar(n+width, male, width, label = 'Male')
ax.set(xlabel = 'Survived', ylabel = 'Amount')
ax.set_xticklabels(['Not Survived', 'Survived'])
ax.set_xticks(n + width /2)
ax.legend(loc = 'best')
plt.show()

