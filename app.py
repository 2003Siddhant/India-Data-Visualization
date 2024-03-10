import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('C:/Users/siddhant sakhare/Documents/Plotly/india.csv')

list_of_state = list(df['State'].unique())
list_of_state.insert(0, 'Overall India')

st.sidebar.title = ('India ka Data Visualization')
Selected_state = st.sidebar.selectbox('Select a State', list_of_state)
primary = st.sidebar.selectbox(
    'Select Primary Parameter', sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox(
    'Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if Selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=Secondary, zoom=4, size_max=35,
                                mapbox_style="carto-positron", width=1100, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == Selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=Secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1100, height=700, hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
