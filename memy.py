import streamlit as st
import pandas as pd

# Function to identify critical servers
def find_critical_servers(df):
    critical_servers = df[(df['Used Memory'] / df['Total Memory'] > 0.9) | (df['Used Swap'] / df['Total Swap'] > 0.9)]
    return critical_servers

# Streamlit UI
st.title('Server Memory Utilization Analyzer')
st.write('Upload an Excel file to analyze server memory utilization data.')

uploaded_file = st.file_uploader('Choose an Excel file', type='xlsx')

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)

    # Display the data
    st.write('Uploaded Data:')
    st.dataframe(df)

    # Find critical servers
    critical_servers = find_critical_servers(df)

    # Display critical servers
    st.write('Critical Servers:')
    st.dataframe(critical_servers)

    # Option to download the critical servers data
    st.download_button(label='Download Critical Servers Data',
                       data=critical_servers.to_csv(index=False),
                       file_name='critical_servers.csv',
                       mime='text/csv')
else:
    st.write('Please upload an Excel file.')

