# Climate-Crop-Sense
Climate crop sense is an predictive analytical model for climate resilience. Here we retrieve real-time data for accurate weather predictions for any particular district, enabling farmers to plan and adapt to changing climate conditions. Here in this project we do recommend an crop by user input about soil details with current weather information. 

## README

### Project Overview
This project is designed to recommend crops based on soil details and provide upcoming weather predictions. The application is built using Python and Streamlit, ensuring an interactive and user-friendly interface.

### Download and Setup Instructions

#### Step 1: Download the Project
Download the project as a ZIP file from the repository.

#### Step 2: Unzip the Project
Unzip the downloaded ZIP file to your desired directory.

#### Step 3: Install Required Libraries
Navigate to the project directory and install the required libraries. The main library needed is Streamlit, along with other dependencies listed in the `requirements.txt` file.

Open your terminal and run the following commands:

```sh
cd /path/to/unzipped/project
pip install -r requirements.txt
```

#### Step 4: Run the Application
After installing all necessary libraries, you can start the application using Streamlit. In the terminal, execute:

```sh
streamlit run main.py
```

### Usage Instructions

1. Open your web browser and go to `http://localhost:8501` to access the application.

2. Select your state and district from the dropdown menus.

3. Provide input about soil details specific to your area.

4. Click the "Predict" button.

5. You will receive a crop recommendation along with its prerequisites and other relevant details.

6. The right sidebar will display the weather forecast for the next 10 days.

### Features

- **State and District Selection:** Users can select their specific location to get tailored recommendations.
- **Soil Details Input:** Users can input soil information to get accurate crop recommendations.
- **Crop Recommendation:** Based on the provided details, the app suggests the most suitable crop.
- **Weather Prediction:** Displays the weather forecast for the upcoming 10 days to aid in planning.

### Dependencies
- Python 3.x
- Python basic ML libraries
- Streamlit

### Contact
For any issues or questions, please contact the project maintainers.

### License
This project is licensed under the GNU License. See the LICENSE file for more details.

---

This README file provides detailed instructions on setting up and running the application. If you follow the steps outlined above, you should be able to successfully use the crop recommendation and weather prediction features of the app.
