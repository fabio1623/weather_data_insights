# Weather Data Analysis Application

This is a Streamlit application that fetches and analyzes weather data for a list of cities provided by the user. It uses a weather API to retrieve current weather data, including temperature, humidity, pressure, and other conditions. The application then provides various insights and visualizations based on the fetched data.

## Features

- **Fetch Weather Data:** Enter a list of cities and retrieve real-time weather data including temperature, humidity, pressure, and more.
- **Data Analysis:** Analyze the fetched weather data to identify:
  - The city with the highest temperature.
  - The city with the lowest humidity.
  - The most common weather condition among the selected cities.
- **Visualizations:** The application includes the following visualizations:
  - **Temperature vs. Humidity:** Scatter plot comparing temperature and humidity.
  - **Temperature and Humidity by Hemisphere:** Box plots displaying temperature and humidity by hemisphere.
  - **Histogram of Temperatures Across Cities:** Histogram showing the distribution of temperatures.
  - **Humidity over Pressure:** Line chart showing humidity levels relative to atmospheric pressure.
  - **Temperature over Pressure:** Line chart comparing temperature and pressure.
  - **Variance between Temperature and Feels-Like Temperature over Pressure:** Box plot showing the variance between actual and feels-like temperatures over pressure.
  - **Wind Speed over Pressure:** Line chart showing wind speed relative to atmospheric pressure.

## Requirements

- Python 3.7 or higher
- Streamlit
- Requests
- Pandas
- Seaborn
- Matplotlib
- API Key for the OpenWeatherMap weather service

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/weather-analysis-app.git
   cd weather-analysis-app
   ```

2. **Install the required packages:**

  ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Weather API key:**

- Sign up for a free API key from OpenWeatherMap service provider (https://openweathermap.org/)
- Add your API key in function.py:

  ```bash
     API_KEY="your_api_key_here"
   ```

4. **Run the application:**

  ```bash
  streamlit run main.py
  ```

## Usage

1. Enter City Names: In the input field, enter the names of cities separated by commas (e.g., New York, London, Tokyo).
2. Fetch Weather Data: Click the "Fetch Weather Data" button to retrieve and analyze the weather data.
3. View Results: The application will display the weather data, analysis results, and various visualizations.

## Error Handling

- If no city names are entered, the application will display an error message.
- If invalid or empty city names are entered, the application will prompt you to enter at least one valid city name.
- If the weather data cannot be retrieved (e.g., due to a network issue or invalid API key), a warning message will be displayed.