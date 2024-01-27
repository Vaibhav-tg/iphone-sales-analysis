import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
data=pd.read_csv("apple_products.csv")
data.rename(columns={
'Number Of Ratings':'no. of rating',
    'Discount Percentage':'discount',
    'Star Reviews':'review',
    'Number Of Reviews':'no. of reviews'
    },inplace=True)
print(data.to_string())
print(data.isnull().sum()) #this will return total number of null values for each column in given data
print(data.describe())
highest_rated=data.sort_values(by=['Star Rating'],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])
# The output of Above code is the top 10 higest rated iphone based on user ratings..
iphone=highest_rated['Product Name'].value_counts()
labels=iphone.index
counts=highest_rated['no. of rating']
fig=px.bar(highest_rated,x=labels,y=counts,title="Top 10 highest rated iphones")
fig.show()
# By using Data visualization technique we can data in graph form instead of table.It helps to understand the data easily
iphone=highest_rated['Product Name'].value_counts()
labels=iphone.index
counts=highest_rated['no. of reviews']
fig=px.bar(highest_rated,x=labels,y=counts,title="Top 10 highest reviews iphones")
fig.show()
#the graph shows the iphones and their reviews
fig=px.scatter(data_frame=data,x="no. of rating",y="Sale Price",size="discount",
               trendline="ols",title="relation between number of rating and sale price")
fig.show()
