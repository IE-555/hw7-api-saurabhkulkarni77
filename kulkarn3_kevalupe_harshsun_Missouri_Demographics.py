#Source(s):  
#URLs for any Websites that were used for this code:
#URLs for code 1)https://dev.socrata.com/foundry/data.mo.gov/3vxz-wrn6
##2)https://pythonspot.com/matplotlib-bar-chart/
##3)https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.pie.html
#4)https://seaborn.pydata.org/generated/seaborn.boxplot.html
#5)https://python-graph-gallery.com/161-custom-matplotlib-donut-plot/
#Data Sources :
#1) https://data.mo.gov/
#2)https://dev.socrata.com/foundry/data.mo.gov/3vxz-wrn6

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sodapy import Socrata
import os
import seaborn as sns
app_token = os.environ.get('APP_TOKEN_ONLINEDATA_ASSIGNMENT')
username = os.environ.get('USER_ONLINEDATA')
password = os.environ.get('PASS_ONLINEDATA')
#authenticated client (needed for non-public datasets):
client = Socrata("data.mo.gov",
                 app_token,
                  username=username,
                  password=password)

results = client.get("3vxz-wrn6")
# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
all_colms = list(results_df.columns)
labels = all_colms[2:]
px = list(results_df.iloc[0])
sizes = px[2:]
bar = list(results_df.iloc[1])
donut = list(results_df.iloc[2])
size_for_bar = bar[2:]
size_for_donut = donut[2:]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.title('Distribution of Deaf and Hard of hearing in Missouri state')
plt.tight_layout()
plt.savefig('figureone.png')
plt.close() 	
objects = labels
y_pos = np.arange(len(objects))
performance = size_for_bar

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Population')
plt.title('Distribution in Adair County')
plt.savefig('figuretwo.png')
plt.close() 

colors = ['yellowgreen', 'gold', 'lightcoral']
explode = (0, 0, 0)  # explode a slice if required
plt.pie(size_for_donut, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True)
        
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.title('Distribution in Andrew')
plt.savefig('figurethree.png')
plt.close()
results_df['est_deaf_1'] = pd.to_numeric(results_df['est_deaf_1'])
results_df['total_population_2010'] = pd.to_numeric(results_df['total_population_2010'])
results_df['est_hoh_9'] = pd.to_numeric(results_df['est_hoh_9'])
results_df['est_deaf_hoh_10'] = pd.to_numeric(results_df['est_deaf_hoh_10'])
results_df = results_df.set_index('county')

df = results_df[results_df['total_population_2010']>100000]
df = df[['total_population_2010']]
df.plot.bar(logy =True, rot =90, title="Distribution of Deaf and Hard of hearing in Missouri state",align='center', alpha=0.5,figsize=(20,10));
plt.savefig('figurefour.png')
plt.close()
df = results_df[results_df['total_population_2010']>100000]
df = df[['total_population_2010','est_deaf_1','est_hoh_9','est_deaf_hoh_10']]
df.plot.bar(rot=90, logy =True, align='center', alpha=0.5, figsize=(20,10))  
plt.savefig('figurefive.png')
plt.close()