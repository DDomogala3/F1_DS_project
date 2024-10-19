import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Formual One Streamlit script


st.title("Formula One Data Analysis: Coming July 2025")
st.header("Performance and Driver Data Analysis of Your Choice")
st.write("Code comes from this Kaggle site. https://www.kaggle.com/code/mansipanchal24/eda-on-f1-data-in-progress")
df_cr = pd.read_csv('constructor_results.csv')


try:
    team_input = st.text_input("What team do you want to analyze:?")
except IndexError:
    print("Index out of range!")
if IndexError:
    print("Team name is not entered!")
else:
    pass

st.write("Please note team names with two words have a '_' in the middle e.g. 'red_bull'")
st.write("Let's look at %s team data" % team_input)
df_cs = pd.read_csv('constructor_standings.csv')
)                   
df_c = pd.read_csv('constructors.csv')

race_data = pd.read_csv('races.csv')
#st.dataframe(race_data)
Haas_id = df_c[df_c['constructorRef'] == 'haas']['constructorId'].values[0]
#Haas_id
team_input = team_input.lower()
try:
    team_id = df_c[df_c['constructorRef'] == team_input]['constructorId'].values[0]
    
   
    
except IndexError:
    st.write("Team name is not entered or is incorrect!")
team_id = df_c[df_c['constructorRef'] == team_input]['constructorId'].values[0]

st.write("Your Team ID is %d" % team_id)

df_cr_team_input = df_cr[df_cr['constructorId'] == team_id]
df_cr_haas = df_cr[df_cr['constructorId'] == Haas_id]
#df_cr_haas
df_cs_haas = df_cs[df_cs['constructorId'] == Haas_id]
#df_cs_haas
df_cs_team_input = df_cs[df_cs['constructorId'] == team_id]


team_input_construct = pd.merge(df_cr_team_input,df_cs_team_input, on=['raceId', 'constructorId'], suffixes=('_results', '_standings'))
st.dataframe(team_input_construct)
#st.dataframe(Haas_construct)


team_data = pd.merge(team_input_construct, race_data, on=['raceId'])

team_input_correlation_matrix = team_data[['points_results', 'points_standings', 'position', 'wins']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(team_input_correlation_matrix, annot=True, cmap='coolwarm')
st.write(plt.title('Correlation Matrix of Performance Metrics for %s'% team_input))
st.pyplot(plt)



df_driv = pd.read_csv('drivers.csv')
df_ds = pd.read_csv('driver_standings.csv')
df_results = pd.read_csv('results.csv')

team_input_results = df_results[df_results['constructorId'] == team_id]
haas_results = df_results[df_results['constructorId'] == Haas_id]

haas_driver_ids = haas_results['driverId'].unique()
team_driver_ids = team_input_results['driverId'].unique()

haas_drivers = df_driv[df_driv['driverId'].isin(haas_driver_ids)]
team_input_drivers = df_driv[df_driv['driverId'].isin(team_driver_ids)]

haas_ds = df_ds[df_ds['driverId'].isin(haas_driver_ids)]
team_input_ds = df_ds[df_ds['driverId'].isin(team_driver_ids)]
team_input_standings_with_names = pd.merge(team_input_results, team_input_drivers, on='driverId',how='left')
haas_standings_with_names = pd.merge(haas_results, haas_drivers, on='driverId', how='left')



team_input_standings_with_names.rename(columns={'forename':'First Name','surname':'Last Name'}, inplace=True)

haas_standings_with_names.rename(columns={'forename': 'First Name', 'surname': 'Last Name'}, inplace=True)
haas_standings_with_names['position'] = pd.to_numeric(haas_standings_with_names['position'], errors='coerce')
team_input_standings_with_names['position'] = pd.to_numeric(team_input_standings_with_names['position'], errors='coerce')

#haas_standings_with_names.describe()
driver_performance = haas_standings_with_names.groupby(['Last Name'])[['points', 'position']].mean().reset_index()
team_input_driver_performance = team_input_standings_with_names.groupby(['Last Name'])[['points', 'position']].mean().reset_index()

fig, ax1 = plt.subplots(figsize=(10,6))

sns.barplot(data=team_input_driver_performance, x='Last Name', y='points', ax=ax1, color='b', alpha=0.6, label='Average Points')
ax1.set_xlabel('Driver')
ax1.set_ylabel('Average Points', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax1.set_xticks(range(len(team_input_driver_performance)))
ax1.set_xticklabels(team_input_driver_performance['Last Name'], rotation=90)

ax2 = ax1.twinx()
sns.lineplot(data=team_input_driver_performance, x='Last Name', y='position', ax=ax2, color='r', marker='o', label='Average Position')

ax2.set_ylabel('Average Position', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Average Points and Positions by Driver')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

st.pyplot(plt)

st.write(team_data.year)
result_by_year_lamda = lambda date,year,metric: data.groupby(year)[metric].mean().reset_index()

#team_input_data = pd.merge(mclaren_construct, race_data, on=['raceId'])

def result_by_year(data, year, metric):
    avg = data.groupby(year)[metric].mean().reset_index()
    return avg



avg_positon_per_year = result_by_year(team_data,'year', 'position')

plt.figure(figsize=(12, 6))
plt.plot(avg_position_per_year['year'], avg_position_per_year['position'], marker='o')
plt.title('Average Finishing Position per Year for %s' % team_input)
plt.xlabel('Year')
plt.ylabel('Average Position')
plt.gca().invert_yaxis()  # Invert y-axis so that lower positions are better
plt.grid(True)
plt.show()

st.divider()





