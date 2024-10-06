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
df_results = pd.read_csv('results.csv')


haas_results = df_results[df_results['constructorId'] == Haas_id]

haas_driver_ids = haas_results['driverId'].unique()

haas_drivers = df_driv[df_driv['driverId'].isin(haas_driver_ids)]
haas_ds = df_ds[df_ds['driverId'].isin(haas_driver_ids)]
haas_standings_with_names = pd.merge(haas_results, haas_drivers, on='driverId', how='left')

#mclaren_standings_with_names = mclaren_standings_with_names[['driverId','forename', 'surname','points','position']]


haas_standings_with_names.rename(columns={'forename': 'First Name', 'surname': 'Last Name'}, inplace=True)
haas_standings_with_names['position'] = pd.to_numeric(haas_standings_with_names['position'], errors='coerce')

haas_standings_with_names.describe()
driver_performance = haas_standings_with_names.groupby(['Last Name'])[['points', 'position']].mean().reset_index()
fig, ax1 = plt.subplots(figsize=(10,6))

sns.barplot(data=driver_performance, x='Last Name', y='points', ax=ax1, color='b', alpha=0.6, label='Average Points')
ax1.set_xlabel('Driver')
ax1.set_ylabel('Average Points', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax1.set_xticks(range(len(driver_performance)))
ax1.set_xticklabels(driver_performance['Last Name'], rotation=90)

ax2 = ax1.twinx()
sns.lineplot(data=driver_performance, x='Last Name', y='position', ax=ax2, color='r', marker='o', label='Average Position')

ax2.set_ylabel('Average Position', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Average Points and Positions by Driver')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

st.pyplot(plt)
