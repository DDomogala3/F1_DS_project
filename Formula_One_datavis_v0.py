import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Formual One Streamlit script


st.write("Formula One Data Analysis:Coming July 2025")


df_cr = pd.read_csv('constructor_results.csv')
st.dataframe(df_cr)
df_cs = pd.read_csv('constructor_standings.csv')
st.dataframe(df_cs)                   
df_c = pd.read_csv('constructors.csv')
st.dataframe(df_c)
race_data = pd.read_csv('races.csv')
st.dataframe(race_data)
Haas_id = df_c[df_c['constructorRef'] == 'haas']['constructorId'].values[0]
st.write(Haas_id)


df_cr_haas = df_cr[df_cr['constructorId'] == Haas_id]
st.write(df_cr_haas)
df_cs_haas = df_cs[df_cs['constructorId'] == Haas_id]
st.write(df_cs_haas)

Haas_construct = pd.merge(df_cr_haas, df_cs_haas, on=['raceId', 'constructorId'], suffixes=('_results', '_standings'))

st.dataframe(Haas_construct)
st.write(Haas_construct.head())
Haas_data = pd.merge(Haas_construct, race_data, on=['raceId'])
st.dataframe(Haas_data)

correlation_matrix = Haas_data[['points_results', 'points_standings', 'position', 'wins']].corr()
st.write(correlation_matrix)
st.write(plt.figure(figsize=(8, 6)))
st.write(sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm'))
st.write(plt.title('Correlation Matrix of Performance Metrics for Haas'))
st.pyplot(plt)
