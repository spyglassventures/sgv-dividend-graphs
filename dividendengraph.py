# Load the Pandas libraries with alias 'pd'
import pandas as pd
from IPython import embed;
import numpy as np

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image

#ToDO:
# replace path with Google Drive
# how to get on only the month in a series?`
# fix ordering with month
# fix image size
# fix fond
# fix colours
# import datetime, fix dates to numnbers, much easier to sort


# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
df = pd.read_csv("Dividenenkalender.csv") # place with Google drive
#embed()

# change to date
df.Datum = pd.to_datetime(df.Datum)
c

# Group by Month
monthdata = df.groupby(df.Datum.dt.strftime('%B'))['Counter'].sum().sort_values()

# Series to DF
monthdata_df = pd.DataFrame({'Datum':monthdata.index, 'list':monthdata.values})





#####################


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

#embed()

# sorting, but wrong
monthdata_df.sort_values(by='Datum') # sort alphabetically

#works, but removes the value
#monthdata_df = pd.DataFrame(monthdata_df, index=months)
#monthdata_df = monthdata_df.loc
#print (monthdata_df)
# geht nich # sorted_month = monthdata.sort_values(by="Month")

# Sorting:
#monthdata_df['Datum'] = pd.Categorical(monthdata_df['Datum'], categories=months, ordered=True)
# fix sorting
#monthdata_df.sort_index(ascending=True)

#####################

#embed()


# Image 2:
# Create monthly divident chart
# plt.bar(monthdata_df.Datum, monthdata_df.list, align='center', alpha=0.5)
# plt.xticks(monthdata_df.Datum) # monthdata
# plt.ylabel('Dividend events in month')
# plt.title('Monthly dividend events 2019')
# plt.show()

# Create accumulated divident chart


# Image 2: include Spyglass logo as Watermark
logo_path = 'logo.png'
im = image.imread(logo_path)
fig, ax= plt.subplots()
myaximage = ax.imshow(im, aspect='auto', extent=(5, 8, 10, 50), alpha=0.85, zorder=-3)   # Widh, Position on horizontal, High_end, High_start # all over the picture with high alpha
                                                #
plt.bar(monthdata_df.Datum, np.cumsum(monthdata_df.list), align='center', alpha=0.5)
plt.ylabel('Cumulative dividend events 2019')
plt.title('Cumulative dividend events 2019')
plt.show()



#embed()

