# Load the Pandas libraries with alias 'pd'
import pandas as pd
from IPython import embed;
import numpy as np

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
import datetime
import seaborn as sns # for matplotlib formatting

#ToDO:
# replace path with Google Drive


# Data Source:
# https://www.finanzen.net/aktien/dividenden/

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
df = pd.read_csv("Dividenenkalender.csv") # place with Google drive




# change to date
dates = pd.to_datetime(df.Datum)

df["Datum"] = pd.to_datetime(df["Datum"])
monthdata = df["Datum"].dt.month

# add counter
#add columns of 1, we can add to get density or for group by
df.insert(0, 'Counter', 1)

# Group by Month
monthdata = df.groupby(df.Datum.dt.strftime('%m'))['Counter'].sum().sort_values()

# sorting
monthdata = monthdata.sort_index(ascending=True)


# Series to DF
monthdata_df = pd.DataFrame({'Datum':monthdata.index, 'list':monthdata.values})

embed()


# Defining CSS
csfont = {'fontname':'Verdana'}
hfont = {'fontname':'Verdana'}
# available: http://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/

sns.set()


# Image 1:
#Create monthly divident chart
logo_path = 'logo.png'
im = image.imread(logo_path)
fig, ax= plt.subplots()
myaximage = ax.imshow(im, aspect='auto', extent=(1, 10, 45, 115), alpha=0.25, zorder=-3)   # Widh, Position on horizontal, High_end, High_start # all over the picture with high alpha
                                                # start of left, 2 seem good
                                                # spread till which value, 10 seems fine
                                                # moving pic start up
                                                # 90 seem good hight
plt.bar(monthdata_df.Datum, monthdata_df.list, align='center', alpha=0.5)   #color = 'darkred', width = 0.8)

plt.xticks(monthdata_df.Datum) # monthdata
plt.ylabel('Dividend Events in Month', **csfont)
plt.xlabel('Month', **csfont)
plt.title('Monthly Dividend events 2019', **hfont)
plt.show()




# Image 2: Cumulative - including Spyglass logo as Watermark
logo_path = 'logo.png'
im = image.imread(logo_path)
fig, ax= plt.subplots()
myaximage = ax.imshow(im, aspect='auto', extent=(1, 10, 120, 350), alpha=0.25, zorder=-3)   # Widh, Position on horizontal, High_end, High_start # all over the picture with high alpha
                                                # start of left, 2 seem good
                                                # spread till which value, 10 seems fine
                                                # moving pic start up
                                                # 90 seem good hight
plt.bar(monthdata_df.Datum, np.cumsum(monthdata_df.list), align='center', alpha=0.5)
plt.ylabel('Cumulative Dividend events 2019', **csfont)
plt.xlabel('Month', **csfont)
plt.title('Cumulative Dividend events 2019', **hfont)
plt.show()
