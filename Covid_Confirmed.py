import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('time_series_covid19_confirmed_US.csv')

# Group the data by 'Province_State' and sum the confirmed cases for each state
state_data = df.groupby('Province_State').sum()

# Extract the dates columns (from 8th column onwards)
date_columns = state_data.columns[4:]

# Calculate the total confirmed cases for each date and store them in a list
total_cases = state_data[date_columns].sum()

# Streamlit app
st.title('COVID-19 Confirmed Cases in the US')

# Date range selection
start_date = st.date_input('Start Date', pd.to_datetime(total_cases.index.min()))
end_date = st.date_input('End Date', pd.to_datetime(total_cases.index.max()))

# Filter data based on selected date range
filtered_cases = total_cases[(total_cases.index >= start_date) & (total_cases.index <= end_date)]

# Plot the line chart using Matplotlib
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_cases.index, filtered_cases, marker='o', linestyle='-', color='blue')
ax.set_xticks(filtered_cases.index[::40])
ax.set_xticklabels(filtered_cases.index[::40].strftime('%Y-%m-%d'), rotation=45)
ax.set_xlabel('Date')
ax.set_ylabel('Total Confirmed Cases')
ax.set_title('Total Confirmed Cases for All States over Time')
ax.grid(True)
st.pyplot(fig)
