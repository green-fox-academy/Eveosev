import pandas as pd
import numpy as np
from datetime import datetime


gg_play_store = pd.read_csv('googleplaystore.csv')


#check the data
gg_play_store = gg_play_store.rename(columns = lambda x: x.replace(' ', '_'))
gg_play_store.columns
gg_play_store.info()
gg_play_store.head()


#Change the type to date columns (str to date)
def changetime(value):
    try:
        time = pd.to_datetime(datetime.strptime(value, '%B %d, %Y')).strftime('%Y-%m-%d')
        return time
    except:
        print(value)
        return value

gg_play_store.Last_Updated = gg_play_store.Last_Updated.apply(changetime)

#check the error row
gg_play_store[gg_play_store.Last_Updated == '1.0.19']

#drop the error row and form a new dataframe
gg_play_store = gg_play_store.drop(gg_play_store[gg_play_store.Last_Updated == '1.0.19'].index)


#Check duplicates
#The number of dupcalicates
sum(gg_play_store.duplicates(subset = None, keep = 'first'))

#drop the duplicates
gg_play_store.drop_duplicates(subset = None, keep = 'first', inplace = True)

"""
Quiz
"""
#List down what we know about the app called "Pixel Draw - Number Art Coloring Book"
gg_play_store[gg_play_store.App == "Pixel Draw - Number Art Coloring Book"]


#List down what we know about apps called "Pixel Draw - Number Art Coloring Book", "Beauty Selfie Camera", "BestCam Selfie-selfie, beauty camera, photo editor"
gg_play_store[gg_play_store.App.isin(["Pixel Draw - Number Art Coloring Book", "Beauty Selfie Camera", "BestCam Selfie-selfie, beauty camera, photo editor"])]


#View all the apps listed before the "Mandala Coloring Book"
index_MCB = gg_play_store[gg_play_store.App == 'Mandala Coloring Book'].index
gg_play_store[0:index_MCB[0]]


#List only the ratings of all the apps between 
#'Paper flowers instructions' and 'Text on Photo - Fonteee'
index_PFI = gg_play_store[gg_play_store.App == 'Paper flowers instructions'].index
index_ToPF = gg_play_store[gg_play_store.App == 'Text on Photo - Fonteee'].index
gg_play_store[index_PFI[0]+1:index_ToPF[0]]


#List all the columns between 'Size' and 'Content Rating'
gg_play_store[['Size', 'Installs', 'Type', 'Price','Content_Rating']]


#What is the average rating of apps in the store?
print(gg_play_store['Rating'].mean())


#What is the ratio of free vs paid?
ratio_f_over_p = sum(gg_play_store['Type'] == 'Free') / sum(gg_play_store['Type'] == 'Paid')
print(ratio_f_over_p)
gg_play_store.groupby('Type').count()['App']


#What is the highest amount of Reviews an app received? And the lowest?
gg_play_store.Reviews = gg_play_store.Reviews.apply(lambda x: int(x))
highest_reviews = max(gg_play_store['Reviews'])
gg_play_store.Reviews.max()
gg_play_store['Reviews'].max()
print(highest_reviews)
lowest_reviews = min(gg_play_store['Reviews'])
print(lowest_reviews)


#What are the ten most recently updated apps?
sorted_df = gg_play_store.sort_values(by = 'Last_Updated', ascending = False)
sorted_df[0:10].App


#Find apps, that is in the top 25% of apps 
# based on ratings and were updated in the last two months of dataset.
last_date = sorted_df.Last_Updated[0]
df_within_2m = sorted_df[sorted_df['Last_Updated'] >= last_date]
length = int(len(gg_play_store) * 0.25)
df2 = sorted_df.sort_values(by = 'Rating', ascending = False)
df2[0:length + 1]


#Which app not to download?
#Find an app which takes the most space on your phone, but is rated poorly (define poorly)?
unique_installs = gg_play_store.drop_duplicates('Installs', inplace = False).Installs

#Now we can check the App with '0' and '0+' Installs
Not_download_app = gg_play_store[(gg_play_store.Installs == '0') | (gg_play_store.Installs == '0+')]
Not_download_app


special_app = gg_play_store[gg_play_store.Size == 'Varies with device']
countable_size_apps = gg_play_store.drop(special_app.index)


#Convert size strings to be float
def change_size(size):
    if 'M' in size:
        value = float(size.split('M')[0])
        return value
    elif 'k' in size:
        value = float(size.split('k')[0]) / 1000
        return value

countable_size_apps.Size = countable_size_apps.Size.apply(change_size)
countable_size_apps.describe(include = 'all')

#From the describle statistics, The app takes most space is Hojiboy Tojiboyev Life Hacks (37M) :
most_space_app = countable_size_apps[countable_size_apps.Size == 37.0]
most_space_app
#Not being rated poorly


# Create a reviews reliability of reviews index, which takes into account, how many reviews does the app have and how high the rating is. What metric do you take? Create as a new field.
gg_play_store_u_reviews = pd.read_csv('googleplaystore_user_reviews.csv')
gg_play_store_u_reviews.columns
gg_play_store_u_reviews.head()
gg_play_store.columns

#Drop meaningless data
notnull_gg_df = gg_play_store_u_reviews[gg_play_store_u_reviews.Translated_Review.notnull()]
notnull_gg_df.groupby('App').count()['Translated_Review']

grouped_data = gg_play_store.groupby('App').sum()[['Rating', 'Reviews']]
grouped_data.to_csv('Reviews_statistics.csv')