import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_KEY = os.getenv('API_KEY')
API_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to fetch weather data
def fetch_weather_data(cities):
    weather_data = []
    progress_text = "Fetching weather data. Please wait."
    progress_bar = st.progress(0, text=progress_text)  # Initialize the progress bar
    total_cities = len(cities)

    for i, city in enumerate(cities):
        try:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            }
            response = requests.get(API_URL, params=params)
            data = response.json()

            if response.status_code == 200:
                weather = {
                    'city': city,
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'condition': data['weather'][0]['main'],
                    'lat': data['coord']['lat'],
                    'lon': data['coord']['lon'],
                    'pressure': data['main']['pressure'],
                    'feels_like': data['main']['feels_like'],
                    'temp_min': data['main']['temp_min'],
                    'temp_max': data['main']['temp_max'],
                    'wind_speed': data['wind']['speed']
                }
                weather_data.append(weather)
            else:
                st.error(f"Error fetching data for {city}: {data['message']}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

        # Update the progress bar
        progress_bar.progress((i + 1) / total_cities, text=progress_text)

    progress_bar.empty()  # Clear the progress bar once fetching is complete

    return pd.DataFrame(weather_data)


# Function to analyze the weather data
def analyze_weather_data(df):
    highest_temp_row = df.loc[df['temperature'].idxmax()]
    lowest_humidity_row = df.loc[df['humidity'].idxmin()]

    highest_temp_city = highest_temp_row['city']
    highest_temp_value = highest_temp_row['temperature']

    lowest_humidity_city = lowest_humidity_row['city']
    lowest_humidity_value = lowest_humidity_row['humidity']

    most_common_condition = df['condition'].mode()[0]

    return highest_temp_city, highest_temp_value, lowest_humidity_city, lowest_humidity_value, most_common_condition


# Function to plot temperature vs. humidity with trend lines
def plot_temp_vs_humidity(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temperature', y='humidity', data=df, hue='condition')
    sns.regplot(x='temperature', y='humidity', data=df, scatter=False, color='red')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Humidity (%)')
    plt.title('Temperature vs. Humidity')
    st.pyplot(plt)


# Function to plot box plots of temperature and humidity by region
def plot_box_plots(df):
    df['region'] = df['lat'].apply(lambda x: 'Northern Hemisphere' if x >= 0 else 'Southern Hemisphere')

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x='region', y='temperature', data=df, ax=axes[0])
    axes[0].set_title('Temperature by Hemisphere')
    axes[0].set_xlabel('Region')
    axes[0].set_ylabel('Temperature (°C)')

    sns.boxplot(x='region', y='humidity', data=df, ax=axes[1])
    axes[1].set_title('Humidity by Hemisphere')
    axes[1].set_xlabel('Region')
    axes[1].set_ylabel('Humidity (%)')

    st.pyplot(fig)


# Function to plot a histogram of temperatures across cities
def plot_temperature_histogram(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['temperature'], bins=10, kde=True)
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Temperatures Across Cities')
    st.pyplot(plt)


# Function to plot humidity over pressure as a line chart
def plot_humidity_over_pressure(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='pressure', y='humidity', data=df, marker='o')
    plt.xlabel('Pressure (hPa)')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity over Pressure')
    st.pyplot(plt)


# Function to plot temperature over pressure as a line chart
def plot_temperature_over_pressure(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='pressure', y='temperature', data=df, marker='o')
    plt.xlabel('Pressure (hPa)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature over Pressure')
    st.pyplot(plt)


# Function to plot variance between temperature and feels-like temperature over pressure as a box plot
def plot_temp_vs_feels_like_over_pressure(df):
    df['temp_diff'] = df['temperature'] - df['feels_like']

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='pressure', y='temp_diff', data=df)
    plt.xlabel('Pressure (hPa)')
    plt.ylabel('Temperature Difference (°C)')
    plt.title('Variance between Temperature and Feels-Like Temperature over Pressure')
    st.pyplot(plt)


# Function to plot wind speed over pressure as a line chart
def plot_wind_speed_over_pressure(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='pressure', y='wind_speed', data=df, marker='o')
    plt.xlabel('Pressure (hPa)')
    plt.ylabel('Wind Speed (m/s)')
    plt.title('Wind Speed over Pressure')
    st.pyplot(plt)