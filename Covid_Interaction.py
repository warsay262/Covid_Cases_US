import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Covid_Cases_2020-2022.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Streamlit app
st.title('COVID-19 confirmed Data')

# Sidebar - State selection
selected_state = st.sidebar.selectbox('Select a State', data['US_States'].unique())

# Filter data for the selected state
filtered_data = data[data['US_States'] == selected_state]

# Display table of filtered data
st.write(f'Selected State: {selected_state}')
st.write(filtered_data[['Date', 'Confirmed']].set_index('Date'))

# Create a line chart using Matplotlib and display it using Streamlit
st.write("### Confirmed COVID-19 Cases Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_data['Date'], filtered_data['Confirmed'], marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Confirmed Cases')
ax.set_title(f'Confirmed COVID-19 Cases in {selected_state}')
plt.xticks(rotation=45)
st.pyplot(fig)

# Add a disclaimer
st.write("Note: This dashboard is for demonstration purposes only and the data used may not be up-to-date.")
