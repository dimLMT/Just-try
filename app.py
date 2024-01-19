import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from io import StringIO

# Add title
st.title("EDA with Streamlit")

@st.cache_data
def load_data(fpath):
    df = pd.read_csv(fpath)
    return df

# load the data 
df = load_data('/content/drive/MyDrive/Prediction_of_Product_Sales/sales_predictions_2023new.csv')
# Display an interactive dataframe
st.header("Displaying a DataFrame")
st.dataframe(df, width=1000)

if st.button("Descriptive Statistics"):
  st.dataframe(df.describe().round(2))

if st.button("Summary Information"):
  # Create a string buffer to capture the content
  buffer = StringIO()
  # Write the info into the buffer
  df.info(buf=buffer)
  # Retrieve the content from the buffer
  summary_info = buffer.getvalue()
  st.text(summary_info)
  
if st.button("Null values"):
  nulls =df.isna().sum()
  st.dataframe(nulls)

################################################
# Divider
st.divider()
st.markdown(':tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:')

import plotly.express as px
import plotly.io as pio
pio.templates.default='seaborn'

# Use plotly for explore functions
def plotly_explore_numeric(df, x):
    fig = px.histogram(df,x=x,marginal='box',title=f'Distribution of {x}', 
                      width=1000, height=500)
    return fig
def plotly_explore_categorical(df, x):
    fig = px.histogram(df,x=x,color=x,title=f'Distribution of {x}', 
                          width=1000, height=500)
    fig.update_layout(showlegend=False)
    return fig

# Add a selectbox for all possible features
columns_to_use=df.columns
column = st.selectbox(label="Select a column", options=columns_to_use)
# Conditional statement to determine which function to use
if df[column].dtype == 'object':
    fig = plotly_explore_categorical(df, column)
else:
    fig = plotly_explore_numeric(df, column)
    
# Display appropriate eda plots
st.plotly_chart(fig)
################################################
# Divider
st.divider()
st.markdown(':tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:')
def plotly_numeric_vs_target(df, x, y, trendline='ols',add_hoverdata=True):
    if add_hoverdata == True:
        hover_data = list(df.columns)
    else: 
        hover_data = None
        
    pfig = px.scatter(df, x=x, y=y,width=800, height=600,
                      hover_data=hover_data,
                      trendline=trendline,
                      trendline_color_override='red',
                      title=f"{x} vs. {y}")
    
    pfig.update_traces(marker=dict(size=3),
                      line=dict(dash='dash'))
    return pfig

def plotly_categorical_vs_target(df, x, y, agg='Avg', width=800, height=600):
    fig = px.strip(df, x=x,y=y, color=x, width=width, height=height,
                   title=f'Compare {agg} {y} by {x}')
    average_values = df.groupby(x)[y].mean().reset_index()
    # Add average lines to the strip plot
    for index, row in average_values.iterrows():
        fig.add_shape(
            dict(
                type='line', xref="x", yref="y",
                x0=index-0.3, y0=row[y], 
                x1=index+0.3, y1=row[y],
                line=dict(color='black', width=3)
            )
        )                
    fig.update_layout(showlegend=False)
    return fig

target='Item_Outlet_Sales'
feature = st.selectbox(label="Select a column (exclude Item_Outlet_Sales)", options=columns_to_use)
# Conditional statement to determine which function to use
if df[feature].dtype == 'object':
    fig_vs  = plotly_categorical_vs_target(df, x = feature, y= target)
else:
    fig_vs  = plotly_numeric_vs_target(df, x = feature, y= target)

# Display appropriate eda plots
st.plotly_chart(fig_vs)