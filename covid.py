import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data
@st.cache
def load_data():
    data = pd.read_csv(r"C:\Users\srikr\Desktop\COLLEGE\Extra\Projects\covid.csv")
    data['Total Confirmed cases'] = pd.to_numeric(data['Total Confirmed cases'], errors='coerce')
    data['Death'] = pd.to_numeric(data['Death'], errors='coerce')
    data['Cured/Discharged/Migrated'] = pd.to_numeric(data['Cured/Discharged/Migrated'], errors='coerce')
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    return data

data = load_data()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Raw Data", "Basic Statistics", "Time Series Analysis", "Geographical Visualization", "State/UT-wise Analysis", "Comparison"])

# Raw Data Page
if page == "Raw Data":
    st.title("COVID-19 Data Analysis - Raw Data")
    st.subheader("Raw Data")
    st.write(data)

# Basic Statistics Page
elif page == "Basic Statistics":
    st.title("COVID-19 Data Analysis - Basic Statistics")
    st.subheader("Basic Statistics")

    # Selection for date range or country name
    option = st.radio("Filter by", ["Date Range", "Country Name"])

    if option == "Date Range":
        start_date = st.date_input("Start Date", value=data['Date'].min().date())
        end_date = st.date_input("End Date", value=data['Date'].max().date())

        # Convert date inputs to datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter data by date range
        mask = (data['Date'] >= start_date) & (data['Date'] <= end_date)
        filtered_data = data[mask]

        st.write(f"### Statistics for Date Range: {start_date.date()} to {end_date.date()}")

        # Descriptive Statistics
        st.write("#### Descriptive Statistics")
        descriptive_stats = filtered_data[['Total Confirmed cases', 'Death', 'Cured/Discharged/Migrated']].describe()
        st.write(descriptive_stats)

        # Percentage Calculations
        st.write("#### Percentage Calculations")
        total_confirmed = filtered_data['Total Confirmed cases'].sum()
        total_deaths = filtered_data['Death'].sum()
        total_recovered = filtered_data['Cured/Discharged/Migrated'].sum()

        death_percentage = (total_deaths / total_confirmed) * 100
        recovery_percentage = (total_recovered / total_confirmed) * 100

        st.write(f"Percentage of Deaths: {death_percentage:.2f}%")
        st.write(f"Percentage of Recovered: {recovery_percentage:.2f}%")

    elif option == "Country Name":
        country = st.selectbox("Select a Country", data['Name of State / UT'].unique())
        
        # Filter data by country name
        filtered_data = data[data['Name of State / UT'] == country]

        st.write(f"### Statistics for {country}")

        # Descriptive Statistics
        st.write("#### Descriptive Statistics")
        descriptive_stats = filtered_data[['Total Confirmed cases', 'Death', 'Cured/Discharged/Migrated']].describe()
        st.write(descriptive_stats)

        # Percentage Calculations
        st.write("#### Percentage Calculations")
        total_confirmed = filtered_data['Total Confirmed cases'].sum()
        total_deaths = filtered_data['Death'].sum()
        total_recovered = filtered_data['Cured/Discharged/Migrated'].sum()

        death_percentage = (total_deaths / total_confirmed) * 100
        recovery_percentage = (total_recovered / total_confirmed) * 100

        st.write(f"Percentage of Deaths: {death_percentage:.2f}%")
        st.write(f"Percentage of Recovered: {recovery_percentage:.2f}%")

# Time Series Analysis Page
elif page == "Time Series Analysis":
    st.title("COVID-19 Data Analysis - Time Series Analysis")
    st.subheader("Time Series Analysis")
    time_series = data.groupby('Date').sum()
    fig, ax = plt.subplots()
    ax.plot(time_series.index, time_series['Total Confirmed cases'], label='Confirmed Cases')
    ax.plot(time_series.index, time_series['Death'], label='Deaths')
    ax.plot(time_series.index, time_series['Cured/Discharged/Migrated'], label='Recovered')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.legend()
    st.pyplot(fig)

# Geographical Visualization Page
elif page == "Geographical Visualization":
    st.title("COVID-19 Data Analysis - Geographical Visualization")
    st.subheader("Geographical Visualization")
    fig = px.scatter_geo(data, lat='Latitude', lon='Longitude', color='Total Confirmed cases',
                         hover_name='Name of State / UT', size='Total Confirmed cases',
                         projection="natural earth", scope='asia')
    fig.update_geos(
        center={"lat": 20.5937, "lon": 78.9629},
        lataxis_range=[5, 35], lonaxis_range=[65, 100]
    )
    st.plotly_chart(fig)

# State/UT-wise Analysis Page
elif page == "State/UT-wise Analysis":
    st.title("COVID-19 Data Analysis - State/UT-wise Analysis")
    st.subheader("State/UT-wise Analysis")
    state = st.selectbox("Select a State/UT", data['Name of State / UT'].unique())
    state_data = data[data['Name of State / UT'] == state]
    st.write(state_data)

# Comparison Page
elif page == "Comparison":
    st.title("COVID-19 Data Analysis - Comparison")
    st.subheader("Comparison")
    states = st.multiselect("Select States/UTs to Compare", data['Name of State / UT'].unique())
    if len(states) > 0:
        comparison_data = data[data['Name of State / UT'].isin(states)]
        fig, ax = plt.subplots()
        for state in states:
            state_data = comparison_data[comparison_data['Name of State / UT'] == state]
            ax.plot(state_data['Date'], state_data['Total Confirmed cases'], label=state)
        ax.set_xlabel('Date')
        ax.set_ylabel('Confirmed Cases')
        ax.legend()
        st.pyplot(fig)
