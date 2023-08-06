import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('time_series_covid19_confirmed_US.csv')

# Group by Province_State (State) and sum the cases for each date
state_data = data.groupby('Province_State').sum().drop(['Admin2'], axis=1)

# Convert the date columns to a proper datetime format
state_data.columns = pd.to_datetime(state_data.columns)

# Transpose the DataFrame to have dates as rows and states as columns
state_data = state_data.transpose()

# Streamlit app
st.title('Total Confirmed COVID-19 Cases Over Time by State')

# Select a state using a dropdown
selected_state = st.selectbox('Select a State:', state_data.columns)

# Filter data for the selected state
state_series = state_data[selected_state]

# Create a line chart using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(state_series.index, state_series.values, marker='o')
ax.set_title(f'Total Confirmed COVID-19 Cases Over Time in {selected_state}')
ax.set_xlabel('Date')
ax.set_ylabel('Total Confirmed Cases')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the chart using Streamlit
st.pyplot(fig)
