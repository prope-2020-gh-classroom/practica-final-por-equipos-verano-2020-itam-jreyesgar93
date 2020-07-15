# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:27:50 2020

@author: joser
"""


import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
directorio = os.getcwd()


df=pd.read_csv(directorio+"\\Video_Games_Sales_as_at_22_Dec_2016.csv")
df.dtypes ### User_Score debería ser float y es objecto
df.User_Score.unique() ## se observa el string "tbd", se cambiará por nan

df.User_Score[df.User_Score=="tbd"]="nan"
df.User_Score=df.User_Score.astype(float)
print(df.columns)

plt.boxplot(df.Critic_Count[~np.isnan(df.Critic_Count)])
plt.hist(df.Critic_Count)
plt.boxplot(df.User_Count[~np.isnan(df.User_Count)])
plt.boxplot(df.Critic_Score[~np.isnan(df.Critic_Score)])



plt.boxplot(df.User_Score[~np.isnan(df.User_Score)])
plt.hist(df.User_Count)
df_summary=df.describe()

