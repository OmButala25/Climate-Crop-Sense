import streamlit as st
import requests
import json
import joblib
from datetime import datetime
from PIL import Image

# Load the saved models
NaiveBayes_model = joblib.load('Saved-Models/NaiveBayes.joblib')

# Function to make prediction
def predict_crop(model, data):
    prediction = model.predict(data)
    return prediction

# Function to fetch live weather data
def get_weather_data(city, forecast=False):
    api_key = "V6X3WLB27JR6N9BA588EPVZ6A"  # Replace with your Visual Crossing Weather API key
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}'
    if forecast:
        url += '&include=fcst'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data 
    else:
        st.error("Failed to fetch weather data.")

# Function to load JSON data for predicted crop
def load_crop_info(crop_name):
    try:
        with open(f'Info_file/{crop_name.lower()}.json', 'r', encoding='utf-8') as f:
            crop_info = json.load(f)
        return crop_info
    except FileNotFoundError:
        return None

# Main UI
def main():

    # Set page configuration
    st.set_page_config(
        page_title="Climate Crop Sense",
        page_icon="🌾",
        layout="wide"
    )

    # Set left and right sidebar
    left_sidebar, right_sidebar = st.columns([2, 1])

    # Left sidebar
    with left_sidebar:
        st.title("Climate Crop Sense")
        
        st.write("")

        # Read districts from JSON file
        with open('districts.json', 'r', encoding='utf-8') as f:
            districts = json.load(f)
        
        # Select state
        state = st.sidebar.selectbox("Select State", list(districts.keys()))

        # Select district based on state selection
        district = st.sidebar.selectbox("Select District", districts[state])

        # Fetch live weather data based on the selected district
        city = district + ", " + state
        weather_data = get_weather_data(city)
        forecast_data = get_weather_data(city, forecast=True)

        if weather_data and forecast_data:
            current_weather = weather_data['days'][0]

            # Display current weather information
            st.write(f"**Current Weather in {city}:**")
            st.write(f"- Temperature: {current_weather['tempmax']}°C")
            st.write(f"- Humidity: {current_weather['humidity']}%")
            st.write(f"- Rainfall: {current_weather['precip']}mm")

            # Nitrogen, Phosphorus, Potassium, pH, and Rainfall Input
            N = st.sidebar.number_input("Nitrogen (N) Level", min_value=0, max_value=100, value=50)
            P = st.sidebar.number_input("Phosphorus (P) Level", min_value=0, max_value=100, value=50)
            K = st.sidebar.number_input("Potassium (K) Level", min_value=0, max_value=100, value=50)
            ph = st.sidebar.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)

            st.write("")  # Add space

            # Prediction button
            if st.sidebar.button("Predict", key="predict_button", help="Click to predict the recommended crop"):
                st.write("")  # Add space
                st.write("Prediction in Progress...")

                # Use live weather data directly in the prediction
                data = [[N, P, K, current_weather['tempmax'], current_weather['humidity'], ph, current_weather['precip']]]

                # Perform prediction using the Naive Bayes model
                NB_prediction = predict_crop(NaiveBayes_model, data)

                # Display predicted crop
                st.subheader("Crop Recommended:")
                st.write("Based on the environmental data provided, the recommended crop is:", NB_prediction[0].capitalize())
                
                try:
                    st.image(f"Crops images/{NB_prediction[0].lower()}.jpg", caption=NB_prediction[0].capitalize(), use_column_width=True)
                    crop_info = load_crop_info(NB_prediction[0])  # Load JSON data for predicted crop
                    if crop_info:
                        st.write("**Crop Information:**")
                        for category, info in crop_info.items():
                            st.subheader(category.replace("_", " ").title())
                            if isinstance(info, dict):
                                for key, value in info.items():
                                    st.write(f"- {key.capitalize()}: {value}")
                            elif isinstance(info, list):
                                for item in info:
                                    st.write(f"- {item}")
                            else:
                                st.write(info)
                    else:
                        st.write(f"No information available for {NB_prediction[0].capitalize()}")
                except FileNotFoundError:
                    st.write(f"Image for {NB_prediction[0].capitalize()} is not available.")
                except Exception as e:
                    st.error(f"An error occurred while displaying the image: {str(e)}")

    # Right sidebar
    with right_sidebar:
        st.title(f"Upcoming Weather in {city}")

        if forecast_data:
            upcoming_weather = forecast_data['days'][1:11]

            for day in upcoming_weather:
                date = datetime.strptime(day['datetime'], '%Y-%m-%d')
                st.write(f"**{date.strftime('%B %d, %Y')}**")
                st.write(f"- Temperature: {day['tempmax']}°C")
                st.write(f"- Humidity: {day['humidity']}%")
                st.write(f"- Rainfall: {day['precip']}mm")
        else:
            st.write("No upcoming weather data available")

        st.write("")  # Add space

    # Set image for prediction
    predict_image = Image.open("crop_predict.jpg")
    st.sidebar.image(predict_image, use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
