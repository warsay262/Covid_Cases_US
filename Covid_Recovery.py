import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
data = pd.read_csv('Covid_Cases_Recovered.csv')

# Remove rows with missing data
data = data.dropna(subset=['Recovered'])

# Get the latest date
latest_date = data['Date'].max()

# Filter data for the latest date
latest_data = data[data['Date'] == latest_date]

# Streamlit app title
st.title('COVID-19 Recovery Statistics')

# Create bar chart for total recovered cases by states
st.write('### Total Recoveries by State (Latest Date)')
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(latest_data['US_States'], latest_data['Recovered'])
ax1.set_xlabel('States')
ax1.set_ylabel('Total Recovered Cases')
ax1.set_title('Total Recoveries by State (Latest Date)')
ax1.set_xticklabels(latest_data['US_States'], rotation=90)
st.pyplot(fig1)

# Calculate recovery rate as a percentage
latest_data['Recovery Rate'] = (latest_data['Recovered'] / latest_data['Confirmed']) * 100

# Create bar chart for recovery rate by states
st.write('### Recovery Rate by State (Latest Date)')
fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.bar(latest_data['US_States'], latest_data['Recovery Rate'])
ax2.set_xlabel('States')
ax2.set_ylabel('Recovery Rate (%)')
ax2.set_title('Recovery Rate by State (Latest Date)')
ax2.set_xticklabels(latest_data['US_States'], rotation=90)
st.pyplot(fig2)
