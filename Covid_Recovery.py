import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Covid_Cases_Recovered.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Remove rows with missing data
data.dropna(subset=['Confirmed', 'Deaths', 'Recovered'], inplace=True)

# Streamlit app
st.title('COVID-19 Recovery Data')

# Get the latest date in the data
latest_date = data['Date'].max()

# Filter data for the latest date
latest_data = data[data['Date'] == latest_date]

# Create a list of states for user selection
states = latest_data['US_States'].unique()
selected_state = st.sidebar.selectbox('Select a State', states)

# Filter data for the selected state
selected_state_data = latest_data[latest_data['US_States'] == selected_state]

# Display recovery rate and total recoveries for the selected state
st.write(f"Latest Date: {latest_date.strftime('%Y-%m-%d')}")
st.write(f"Selected State: {selected_state}")
st.write(f"Recovery Rate: {selected_state_data['Recovered'].values[0] / selected_state_data['Confirmed'].values[0] * 100:.2f}%")
st.write(f"Total Recoveries: {selected_state_data['Recovered'].values[0]}")

# Create bar chart for latest recovery rates by states
recovery_rates = latest_data['Recovered'] / latest_data['Confirmed'] * 100
recovery_rates_df = pd.DataFrame({'State': latest_data['US_States'], 'Recovery Rate': recovery_rates})

# Create bar chart for total recoveries by state
total_recoveries_df = latest_data.groupby('US_States')['Recovered'].sum().reset_index()
st.write("### Total Recoveries by State")
fig_recoveries, ax_recoveries = plt.subplots(figsize=(10, 6))
ax_recoveries.bar(total_recoveries_df['US_States'], total_recoveries_df['Recovered'])
ax_recoveries.set_xlabel('States')
ax_recoveries.set_ylabel('Total Recoveries')
ax_recoveries.set_title('Total Recoveries by State')
plt.xticks(rotation=45)
st.pyplot(fig_recoveries)
