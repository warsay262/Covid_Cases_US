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

# Streamlit App
st.title('COVID-19 Confirmed Cases Analysis')
st.sidebar.header('Date Range Selector')

# Date range selection
start_date = st.sidebar.date_input('Start Date', pd.to_datetime(date_columns.min()))
end_date = st.sidebar.date_input('End Date', pd.to_datetime(date_columns.max()))

# Filter data based on selected date range
filtered_cases = total_cases.loc[start_date:end_date]

# Plot the data using Matplotlib
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_cases.index, filtered_cases, marker='o', linestyle='-', color='blue')
ax.set_xticks(filtered_cases.index)
ax.set_xticklabels(filtered_cases.index.strftime('%Y-%m-%d'), rotation=45)
ax.set_xlabel('Date')
ax.set_ylabel('Total Confirmed Cases')
ax.set_title('Total Confirmed Cases for All States over Time')
ax.grid(True)

# Display the plot using Streamlit
st.pyplot(fig)
