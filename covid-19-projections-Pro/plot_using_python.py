# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB.
import matplotlib.pyplot as plt
import pandas as pd

URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
# then put the read me file in dfl Variable
df1 = pd.read_csv(URL_DATASET)
# then from df_india find out the country = India 
df_india = df1[df1['Country'] == 'India']
# then print out the df_india country first line 
print(df_india.head(3))
# size of graphy screen size
plt.rcParams["figure.figsize"]=15,15

# Plot column 'Confirmed'
df_india.plot(kind = 'bar', x = 'Date', y = 'Confirmed', color = 'blue')

# To get the current figure number in Python's Matplotlib, we can use plt. gcf(). number
ax1 = plt.gca()
# plot the graphy using plot funcation 
df_india.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = ax1)
plt.show()


