import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Formual One Streamlit script


st.write("Formula One Data Analysis:Coming July 2025")


df_cr = pd.read_csv('constructor_results.csv')
df_cs = pd.read_csv('constructor_standings.csv')
df_c = pd.read_csv('constructors.csv')
race_data = pd.read_csv('races.csv')

Haas_id = df_c[df_c['constructorRef'] == 'haas']['constructorId'].values[0]


df_cr_haas = df_cr[df_cr['constructorId'] == Haas_id]
df_cs_haas = df_cs[df_cs['constructorId'] == Haas_id]

Haas_construct = pd.merge(df_cr_haas, df_cs_haas, on=['raceId', 'constructorId'], suffixes=('_results', '_standings'))
Haas_construct.head()
Haas_data = pd.merge(Haas_construct, race_data, on=['raceId'])


correlation_matrix = Haas_data[['points_results', 'points_standings', 'position', 'wins']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Performance Metrics for Haas')
plt.show()
