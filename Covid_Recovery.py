import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('Covid_Cases_Recovered.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Remove rows with missing data
data.dropna(subset=['Recovered'], inplace=True)

# Get the latest date
latest_date = data['Date'].max()

# Streamlit app
st.title('COVID-19 Recovery Statistics')

# Sidebar - State selection
selected_state = st.sidebar.selectbox('Select a State', data['US_States'].unique())

# Filter data for the selected state and latest date
filtered_data = data[(data['US_States'] == selected_state) & (data['Date'] == latest_date)]

# Display total recovery for the selected state and latest date
st.write(f"Total Recovery in {selected_state} as of {latest_date}: {int(filtered_data['Recovered'])}")

# Calculate recovery rate and display it
recovery_rate = (filtered_data['Recovered'] / filtered_data['Confirmed']) * 100
st.write(f"Recovery Rate in {selected_state} as of {latest_date}: {recovery_rate:.2f}%")

# Create bar chart for latest recovery rate by states
st.write("### Latest Recovery Rate by States")
latest_recovery_rates = data[data['Date'] == latest_date]
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(latest_recovery_rates['US_States'], (latest_recovery_rates['Recovered'] / latest_recovery_rates['Confirmed']) * 100)
ax.set_xticklabels(latest_recovery_rates['US_States'], rotation=90)
ax.set_xlabel('States')
ax.set_ylabel('Recovery Rate (%)')
ax.set_title('Latest Recovery Rate by States')
st.pyplot(fig)

# Create bar chart for latest recovery date by states
st.write("### Latest Recovery Date by States")
latest_recovery_dates = data.groupby('US_States')['Date'].max().reset_index()
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(latest_recovery_dates['US_States'], latest_recovery_dates['Date'])
ax.set_xticklabels(latest_recovery_dates['US_States'], rotation=90)
ax.set_xlabel('States')
ax.set_ylabel('Latest Recovery Date')
ax.set_title('Latest Recovery Date by States')
st.pyplot(fig)

# Add a disclaimer
st.write("Note: This dashboard is for demonstration purposes only and the data used may not be up-to-date.")
