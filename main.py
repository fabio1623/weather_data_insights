import streamlit as st
import functions


def get_weather_data(user_input):
    if not user_input:
        return "Please enter at least one city name."

    cities = [city.strip() for city in user_input.split(',') if city.strip()]
    if not cities:
        return "Please enter at least one valid city name."

    weather_df = functions.fetch_weather_data(cities)
    if weather_df.empty:
        return "No weather data available for the selected cities."

    return weather_df


def display_weather_data(df):
    st.subheader("Weather Data")
    st.dataframe(df, use_container_width=True)


def display_analysis_results(df):
    highest_temp_city, highest_temp_value, lowest_humidity_city, lowest_humidity_value, most_common_condition = functions.analyze_weather_data(
        df)

    st.subheader("Analysis Results")
    st.markdown(f"🌡️ City with the highest temperature: :red[{highest_temp_city} ({highest_temp_value}°C)]")
    st.markdown(f"💧 City with the lowest humidity: :blue[{lowest_humidity_city} ({lowest_humidity_value}%)]")
    st.markdown(f"🌤️ Most common weather condition: :green[{most_common_condition}]")


def display_plots(df):
    st.subheader("Temperature vs. Humidity")
    functions.plot_temp_vs_humidity(df)

    st.subheader("Temperature and Humidity by Hemisphere")
    functions.plot_box_plots(df)

    st.subheader("Histogram of Temperatures Across Cities")
    functions.plot_temperature_histogram(df)

    st.subheader("Humidity over Pressure")
    functions.plot_humidity_over_pressure(df)

    st.subheader("Temperature over Pressure")
    functions.plot_temperature_over_pressure(df)

    st.subheader("Variance between Temperature and Feels-Like Temperature over Pressure")
    functions.plot_temp_vs_feels_like_over_pressure(df)

    st.subheader("Wind Speed over Pressure")
    functions.plot_wind_speed_over_pressure(df)


def main():
    st.title("Weather Data Analysis")

    st.success('For example: New York, London, Tokyo, Delhi, Sydney, Sao Paulo, Cairo, Moscow', icon="👇")
    cities_input = st.text_input("Enter cities (comma-separated)",
                                 placeholder="e.g., New York, London, Tokyo, Delhi, Sydney, Sao Paulo, Cairo, Moscow")

    if st.button("Fetch Weather Data"):
        weather_df = get_weather_data(cities_input)
        if isinstance(weather_df, str):
            st.warning(weather_df)
            st.stop()

        display_weather_data(weather_df)
        display_analysis_results(weather_df)
        display_plots(weather_df)


if __name__ == "__main__":
    main()