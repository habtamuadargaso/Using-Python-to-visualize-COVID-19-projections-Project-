# instal python library pip3 install pycountry 
# pycountry provides the ISO databases for the standards
import pycountry
import plotly.express as px
import pandas as pd
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
# read the file csv and put in df1
df1 = pd.read_csv(URL_DATASET)
# Get first 3 entries in the dataframe
print(df1.head(3))  
# Get last 3 entries in the dataframe
print(df1.tail(3))  






from asyncore import read
import csv
from re import X
from turtle import color
import pycountry

import plotly.express as px
import pandas as pd

import matplotlib.pyplot as plt

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
# Get first 3 entries in the dataframe 

# from this data select one country data For example 'Zimbabwe'
df_zimbabwe =df1[df1['Country'] == ' Zimbabwe']
print(df1.head(3)) 

# plot column 'Confirmed'
df_zimbabwe.plot(kind ='bar', x = 'Date', y = 'Confirmed', color= 'blue')
# Get last 3 entries in the dataframe

ax1 = plt.gca()
df_zimbabwe.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = ax1)
plt.show()










