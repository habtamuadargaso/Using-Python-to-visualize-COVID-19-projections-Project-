import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(URL_DATASET, usecols = ['Date', 'Country', 'Confirmed'])


# Create list of all dates
list_dates = df['Date'].unique()

#print(list_dates) 

#The subplot() function takes three arguments that describes the layout of the figure.

#The layout is organized in rows and columns, which are represented by the first and second argument
# 15 row and 8 colunm
fig, ax = plt.subplots(figsize=(15, 8))

# We will animate for these 5 countries only

list_countries = ['India', 'China', 'US', 'Italy', 'Spain']

# colors for the 5 horizontal bars
list_colors = ['black', 'red', 'green', 'blue', 'yellow']


# plot_bar() is the call back function used in FuncAnimation class object
def plot_bar(some_date):
    df2 = df[df['Date'].eq(some_date)]
    ax.clear()
   
# Only take Confirmed column in descending order
    df3 = df2.sort_values(by = 'Confirmed', ascending = False)
    
# Select the top 5 Confirmed countries from above list 
    df4 = df3[df3['Country'].isin(list_countries)]
    
    print(df4)  # Uncomment to see that dat is only for 5 countries
    sleep(3)  # To slow down the animation
    # using the ax.barh() makes a horizontal bar plot.
    return ax.barh(df4['Country'], df4['Confirmed'], color= list_colors)


my_anim = animation.FuncAnimation(fig = fig, func = plot_bar,
                    frames= list_dates, blit=True,
                    interval=20)


path_mp4 = r'/Users/atnafudargaso/Documents/git_work/Python to Visualize COVID-19 projections/Using-Python-to-visualize-COVID-19-projections-Project-/covid-19-projections-Pro/Y2mate.mx-MP4 Short Meditation Music   3 Minute Relaxation, Calming(360p).mp4'  
#my_anim.save(path_mp4, fps=30, extra_args=['-vcodec', 'libx264']) 
#my_anim.save(filename = path_mp4, writer = 'ffmpeg',
#            fps=30,

#             extra_args= ['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
plt.show()