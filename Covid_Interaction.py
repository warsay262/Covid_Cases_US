import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('Covid_Cases_2020-2022.csv')

# Create a Streamlit sidebar with state and year selection
st.sidebar.title("COVID-19 Dashboard")
selected_state = st.sidebar.selectbox("Select a state", data['US_States'].unique())
selected_year = st.sidebar.selectbox("Select a year", [2020, 2021, 2022])

# Filter the data based on the selected state and year
filtered_data = data[(data['US_States'] == selected_state) & (data['Date'].str.endswith(str(selected_year)))]

# Calculate the total confirmed cases
total_confirmed = filtered_data['Confirmed'].sum()

# Display the total confirmed cases
st.write(f"Total confirmed cases in {selected_state} in {selected_year}: {total_confirmed}")

# Create a line chart for confirmed cases over the years
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Confirmed'], marker='o')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title(f'Confirmed Cases in {selected_state} ({selected_year})')
st.pyplot(plt)
