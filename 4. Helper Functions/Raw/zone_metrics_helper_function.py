# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:16:07 2019

@author: Gopalkrishnan
"""

#Importing pandas
import pandas as pd
#Reading csv file
heart_rate=pd.read_csv('Running_09-55-32.csv')
heart_rate.info()
#Function
def helper_func_zone(age,heart_rate_with_zone):
    heart_rate_with_zone['Zone_Level']=0
    heart_rate_max=220-age
    heart_rate_with_zone.loc[heart_rate_with_zone.heartRate>=(heart_rate_max-20),'Zone_Level'] = 5
    heart_rate_with_zone.loc[((heart_rate_max-40<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-20)),'Zone_Level'] = 4
    heart_rate_with_zone.loc[((heart_rate_max-60<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-40)),'Zone_Level'] = 3
    heart_rate_with_zone.loc[((heart_rate_max-80<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-60)),'Zone_Level'] = 2
    heart_rate_with_zone.loc[((heart_rate_max-100<=heart_rate_with_zone['heartRate']) & (heart_rate_with_zone['heartRate']<=heart_rate_max-80)),'Zone_Level'] =1
    return(heart_rate_with_zone)

custom_activity_1=helper_func_zone(20,heart_rate)
                    
                
            
