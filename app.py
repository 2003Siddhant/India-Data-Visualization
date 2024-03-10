import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('C:/Users/siddhant sakhare/Documents/Plotly/india.csv')

st.sidebar.title = ('India ka Data Visualization')
