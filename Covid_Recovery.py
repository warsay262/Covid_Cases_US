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

# Dropdown to select state
selected_state = st.selectbox('Select a state:', latest_data['US_States'])

# Filter data for selected state
selected_state_data = latest_data[latest_data['US_States'] == selected_state]

# Calculate recovery rate as a percentage
recovery_rate = (selected_state_data['Recovered'] / selected_state_data['Confirmed']) * 100

# Display recovery rate and total recovered cases for selected state
st.write(f"Recovery Rate in {selected_state} as of {latest_date}: {recovery_rate.values[0]:.2f}%")
st.write(f"Total Recovered Cases in {selected_state} as of {latest_date}: {selected_state_data['Recovered'].values[0]}")

# Create bar chart for total recovered cases by state
st.write('### Total Recoveries by State (Latest Date)')
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(latest_data['US_States'], latest_data['Recovered'])
ax1.set_xlabel('States')
ax1.set_ylabel('Total Recovered Cases')
ax1.set_title('Total Recoveries by State (Latest Date)')
ax1.set_xticklabels(latest_data['US_States'], rotation=90)
st.pyplot(fig1)

# Create bar chart for recovery rate by state
st.write('### Recovery Rate by State (Latest Date)')
fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.bar(latest_data['US_States'], latest_data['Recovery Rate'])
ax2.set_xlabel('States')
ax2.set_ylabel('Recovery Rate (%)')
ax2.set_title('Recovery Rate by State (Latest Date)')
ax2.set_xticklabels(latest_data['US_States'], rotation=90)
st.pyplot(fig2)
