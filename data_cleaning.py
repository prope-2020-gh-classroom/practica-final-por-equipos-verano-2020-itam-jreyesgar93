# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:27:50 2020

@author: joser
"""


import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


"""Carga de datos"""
directorio = os.getcwd() ### Necesario estar en el directorio del programa
df=pd.read_csv(directorio+"\\Video_Games_Sales_as_at_22_Dec_2016.csv")


"""Exploración inicial de los datos"""

df.dtypes ### User_Score debería ser float y es objecto
df.isna().sum() ### Identificar los NA

df.dropna(subset=["Name","Year_of_Release"],inplace=True) ## Eliminamos los NAN de año y nombre
df.reset_index()





df.User_Score.unique() ## se observa el string "tbd", se cambiará por nan
df_summary=df.describe()

 ## para tener la misma escala que critic score


df.User_Score[df.User_Score=="tbd"]="nan"
df.User_Score=df.User_Score.astype(float)
df.User_Score=df.User_Score.transform(lambda x: x*10)
                                      
                                      
                                      
                                      
print(df.columns)
    
"""Exploración de Datos Numéricos Principales"""

fig1,axs=plt.subplots(1,2)
fig1.suptitle("Box-Plot of Scores")
axs[0].boxplot(df.Critic_Score[~np.isnan(df.Critic_Score)])
axs[0].set_xticklabels(["Critic Score"])
axs[1].boxplot(df.User_Score[~np.isnan(df.User_Score)])
axs[1].set_xticklabels(["User Score"])

num_data_summary=dict({"Critic_Score":df.Critic_Score.describe(),
                  "User_Score":df.User_Score.describe()})



"""Exploración de datos Categóricos"""

cat_data_counts=dict({"Platform":df.Platform.value_counts(),
                  "Year_of_Release":df.Year_of_Release.value_counts(),
                  "Genre":df.Genre.value_counts(),
                  "Publisher":df.Publisher.value_counts(),
                  "Rating":df.Rating.value_counts()})








