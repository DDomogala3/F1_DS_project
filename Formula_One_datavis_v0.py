import streamlit as st
import pandas as pd
import numpy as np
#Formual One Streamlit script


st.write("Formula One Data Analysis:Coming July 2025")


df_cr = pd.read_csv('constructor_results.csv')
df_cs = pd.read_csv('constructor_standings.csv')
df_c = pd.read_csv('constructors.csv')
race_data = pd.read_csv('races.csv')

Haas_id = df_c[df_c['constructorRef'] == 'haas']['constructorId'].values[0]




