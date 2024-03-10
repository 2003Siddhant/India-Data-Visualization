import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('C:/Users/siddhant sakhare/Documents/Plotly/india.csv')

list_of_state = list(df['State'].unique())
list_of_state.insert(0, 'Overall India')

st.sidebar.title = ('India ka Data Visualization')
st.sidebar.selectbox('Select a State', list_of_state)
