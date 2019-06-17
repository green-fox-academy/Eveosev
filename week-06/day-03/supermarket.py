import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime

%matplotlib inline
Sales = pd.read_excel('Superstore Sales.xls', index_col=0)

Sales = Sales.rename(columns = lambda x: x.replace(' ', '_').lower())
Sales.head()
Sales.describe()
Sales.info()
Sales.columns


# A) What is the percentage contribution of each region to overall sales?
sizes = Sales.groupby('region').sum().sales
labels = Sales.region.unique()
fig1, ax1 = plt.subplots()
explode = (sizes == sizes.max()) / 10
ax1.pie(sizes, labels = labels, shadow = False, 
        startangle=90, autopct='%1.1f%%',
        explode = explode)
ax1.axis('equal')
ax1.set_title('Percentage contribution of each region to overall sales')
plt.show()


# B) What are the overal sales month by month?
Sales.sort_values(by = 'order_date', inplace = True)
time = np.array(Sales.order_date.unique())
sales_amount = np.array(Sales.groupby('order_date').sum().sales)
# x_time = [time[0], time[len(time) // 2],time[-1]]
# xticks = tuple(map(lambda x: pd.to_datetime(x).strftime('%Y-%m'), x_time))
ax = plt.plot(time, sales_amount, 'm')
plt.title('Overal sales (per month)')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.xticks(rotation = 'vertical')
plt.show()


# C) Which category brought the highest profits?
category = Sales['product_sub-category'].unique()
profits = Sales.groupby('product_sub-category').sum().profit
fig, ax = plt.subplots()
ax.bar(category, profits, alpha = 0.5)
ax.set_xticklabels(labels = category, rotation = 90)
plt.show()


# D)Map the amount of high-priority shipments 
# within 2010 on a timeline.
#Extract the data in 2010
Sales_2010 = Sales[(Sales.order_date > pd.to_datetime('2010')) & (Sales.order_date < pd.to_datetime('2011'))]
Sales_2010_High = Sales_2010[Sales_2010.order_priority == 'High']

#Group data
# priority = np.array(Sales_2010[Sales_2010.order_priority == 'High'].groupby('order_date').sum().order_quantity)

#It is better to group data monthly
Sales_2010_High.order_date = Sales_2010_High.order_date.apply(lambda x: pd.to_datetime(x).strftime('%Y-%m'))
priority = np.array(Sales_2010_High.groupby('order_date').sum().order_quantity)
timeline = Sales_2010_High.order_date.unique()
fig_D, ax_D = plt.subplots()
ax_D.plot(timeline, priority)
ax_D.set(xlabel = 'Time', ylabel = 'Shipment Quantity')
ax_D.set_xticklabels(labels = timeline, rotation = 45)
plt.show()


# E) Graph out the minimum and maximum shipping costs per container type.
shipping_cost = np.array(Sales.groupby('product_container').shipping_cost)
container = []
plot_data = []
for i in shipping_cost:
    plot_data.append(i[1])
    container.append(i[0])
fig_E, ax_E = plt.subplots()
ax_E.boxplot(plot_data)
ax_E.set_xticklabels(container, rotation = 45)
plt.show()


# F) Compare profits per category amongst the different regions
df = pd.DataFrame(Sales.groupby(['product_sub-category', 'region']).sum().profit)
category = np.array(df.index.levels[0])
region = np.array(df.index.levels[1])



