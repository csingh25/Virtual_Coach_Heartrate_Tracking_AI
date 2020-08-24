# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 19:08:54 2019

@author: Gopalkrishnan
"""



#Importing pandas
import pandas as pd
#Reading csv file
heart_rate=pd.read_csv('Running_09-55-32.csv')
heart_rate.info()
import numpy as np
from matplotlib import pyplot as plt

plt.rcdefaults()
ax = plt.subplots()
def helper_func_zone(age,heart_rate_with_zone):
    heart_rate_with_zone['Zone_Level']=0
    heart_rate_max=220-age
    heart_rate_with_zone.loc[heart_rate_with_zone.heartRate>=(heart_rate_max-20),'Zone_Level'] = 5
    heart_rate_with_zone.loc[((heart_rate_max-40<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-20)),'Zone_Level'] = 4
    heart_rate_with_zone.loc[((heart_rate_max-60<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-40)),'Zone_Level'] = 3
    heart_rate_with_zone.loc[((heart_rate_max-80<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-60)),'Zone_Level'] = 2
    heart_rate_with_zone.loc[((heart_rate_max-100<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-80)),'Zone_Level'] =1
    return(heart_rate_with_zone)

custom_activity_3=helper_func_zone(27,heart_rate)
zone=heart_rate.groupby('Zone_Level').size()
zone_df=zone.to_frame()
zone_df.rename(columns = {0:'Time'}, inplace = True)
x=zone_df
y=[0,1,2,3,4,5]
y_pos = np.arange(len(x))
plt.barh(y_pos, x)
plt.yticks(y_pos, y)
plt.show()

plt.barh(y,x,align='center')
plt.invert_yaxis()  # labels read top-to-bottom
plt.set_xlabel('Time_Duration')
plt.set_ylabel('Zone_level')
plt.set_title('For how many mins the user stays in that particular zone')
plt.show()

def helper_func_zone_vis(heart_rate_with_zone):
    x=custom_activity_3['time']
    y=custom_activity_3['Zone_Level']
    plt.title('For how many mins the user stays in that particular zone')
    plt.xlabel('Time_Duration')
    plt.ylabel('Zone_level')
    plt.plot(x,y)
    vis=plt.show()
    return vis

helper_func_zone_vis(heart_rate)



x=custom_activity_3['time']
y=custom_activity_3['Zone_Level']
#plt.figure(figsize=(7.5,7.5))
plt.title("Matplotlib demo")
plt.xlabel("X axis caption")
plt.ylabel("Y axis caption")
plt.plot(x,y)
plt.show()
