#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import os

def zonewise_duration_plot(activitycount):
    # Values of each group
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import rc
    import os
    zone0 = []
    zone1 = []
    zone2 = []
    zone3 = []
    zone4 = []
    zone5 = []
    names=[]
    i=0
    r=[]
    zone={}
    # NOTE : Change the path as per the location of datasets
    dataSetsPath="C:/Users/17167/Desktop/Code/activity_dataset"
    directory = os.path.join(os.getcwd(),dataSetsPath)
    for root,dirs,files in os.walk(directory):
        for file in files:
            zone=[]
            if file.endswith(".csv"):
                filePath=dataSetsPath+"/"+file
                name= file.lower().replace('.csv', '')
                lenname=len(name)
                names.append(name[8:lenname])
                activity = pd.read_csv(filePath)
                custom_activity_3=helper_func_zone(age,activity)
                zone=custom_activity_3.groupby('Zone_Level').size()
                zone0.append(0)
                zone1.append(0)
                zone2.append(0)
                zone3.append(0)
                zone4.append(0)
                zone5.append(0)
                r.append(i)
                if 0 in zone:
                    zone0[i]=zone[0]
                if 1 in zone:
                    zone1[i]=zone[1]
                if 2 in zone:
                    zone2[i]=zone[2]
                if 3 in zone:
                    zone3[i]=zone[3]
                if 4 in zone:
                    zone4[i]=zone[4]
                if 5 in zone:
                    zone5[i]=zone[5]
                i=i+1
                if(activitycount== i+1):
                    break
                
    
    rc('font', weight='bold')
    # height of zone 0 -5
    zonesupto4 = np.add(np.add(np.add(np.add(zone0,zone1),zone2),zone3),zone4)
    zonesupto3 = np.add(np.add(np.add(zone0,zone1),zone2),zone3)
    zonesupto2 = np.add(np.add(zone0,zone1),zone2)
    zonesupto1 = np.add(zone0,zone1)
 
    # Names of activity and zone width
    zoneWidth = .5
 
    # Create brown bars
    plt.bar(r, zone0, color='#7f6d5f', edgecolor='white', width=zoneWidth)
    # Create green bars (middle), on top of the firs ones
    plt.bar(r, zone1, bottom=zone0, color='#557f2d', edgecolor='white', width=zoneWidth)
    # Create green bars (top)
    plt.bar(r, zone2, bottom=zonesupto1, color='#2d7f5e', edgecolor='white', width=zoneWidth)
    # Create blue bars (top)
    plt.bar(r, zone3, bottom=zonesupto2, color='#00a2f5', edgecolor='white', width=zoneWidth)
    # Create yellow bars (top)
    plt.bar(r, zone4, bottom=zonesupto3, color='#cfd623', edgecolor='white', width=zoneWidth)
    # Create red bars (top)
    plt.bar(r, zone5, bottom=zonesupto4, color='#f51b00', edgecolor='white', width=zoneWidth)
    labels=['Zone 0','Zone 1','Zone 2','Zone 3','Zone 4','Zone 5']
    # Custom X axis
    plt.xticks(r, names, fontweight='bold',rotation=90)
    plt.xlabel("Activities")
    plt.ylabel("Time spent in each zone")
    plt.title("Time spent by the user in various zones per activity")
    plt.legend(labels)
 
    # Show graphic
    plt.show()

   
   


# In[ ]:


# Pass number of activities. Adding flexibility to have as many activities needed to be displayed.
zonewise_duration_plot(12)

