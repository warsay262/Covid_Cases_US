import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Covid_Cases_2020-2022.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Streamlit app
st.title('Interactive COVID-19 Dashboard')

# Sidebar - State selection and year range
selected_state = st.sidebar.selectbox('Select a State', data['US_States'].unique())
selected_year_range = st.sidebar.slider('Select Year Range', 2020, 2022, (2020, 2022))

# Filter data based on selected state and year range
filtered_data = data[(data['US_States'] == selected_state) & (data['Date'].dt.year >= selected_year_range[0]) & (data['Date'].dt.year <= selected_year_range[1])]

# Display table of filtered data
st.write(f'Selected State: {selected_state}')
st.write(f'Selected Year Range: {selected_year_range[0]} - {selected_year_range[1]}')
st.write(filtered_data[['Date', 'Confirmed']].set_index('Date'))

# Group data by date and calculate total confirmed cases
daily_cases = filtered_data.groupby('Date')['Confirmed'].sum()

# Create a line chart using Matplotlib and display it using Streamlit
st.write("### Confirmed COVID-19 Cases Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(daily_cases.index, daily_cases.values, marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Confirmed Cases')
ax.set_title('Confirmed COVID-19 Cases Over Time')

# Annotate the chart with selected state and date range
annotation_text = f'Selected State: {selected_state}\nYear Range: {selected_year_range[0]} - {selected_year_range[1]}'
ax.annotate(annotation_text, xy=(0.5, 0.05), xycoords='axes fraction', fontsize=10, ha='center', color='gray')

plt.xticks(rotation=45)
st.pyplot(fig)

# Add a disclaimer
st.write("Note: This dashboard is for demonstration purposes only and the data used may not be up-to-date.")
