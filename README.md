Crop Yield Prediction Per Country
=================================

This is a web-based application designed to predict crop yield based on various agricultural features such as year, average rainfall, pesticide usage, average temperature, area (country), and crop type (item). The application uses a pre-trained machine learning model and a Flask backend to provide predictions through an interactive user interface.

Overview
--------

*   **Purpose**: Predict crop yield (in hg/ha) using input features like year, rainfall, pesticides, temperature, area, and crop type.
    
*   **Technology Stack**: Python, Flask, HTML/CSS, pandas, numpy, scikit-learn.
    
*   **Model**: A pre-trained Decision Tree Regressor model saved as dtr.pkl, with a preprocessor saved as preprocessor.pkl.
    
*   **Interface**: A responsive web interface with dropdowns for categorical data and text inputs for numerical data.
    

Features
--------

*   Dropdown menus for selecting Year, Area (country), and Item (crop type) based on historical data.
    
*   Text inputs for Average Rainfall, Pesticides, and Average Temperature.
    
*   Real-time prediction display including all input features and the predicted yield.
    
*   Attractive and user-friendly design with a dark theme and color-coded sections.
    

Prerequisites
-------------

Before running the project, ensure you have the following installed:

*   **Python 3.x**
    
*   **pip** (Python package manager)
    

### Required Python Packages

Install the necessary dependencies using the following command:

bash

pip install flask numpy pandas scikit-learn

**File Structure**
------------------

text

crop-yield-prediction/│├── app.py # Flask application backend├── index.html # Frontend HTML template with CSS├── yield\_df.csv # Dataset with crop yield data├── dtr.pkl # Pre-trained model file├── preprocessor.pkl # Pre-trained preprocessor file├── README.md # This file└── (optional) requirements.txt # Python dependencies

Usage
-----

1.  **Run the Application**Navigate to the project directory and start the Flask server: bash python app.py
    
2.  **Access the Interface**Open a web browser and go to http://127.0.0.1:5000/.
    
3.  **Input Data**
    
    *   Select a Year from the dropdown.
        
    *   Enter Average Rainfall (mm/year), Pesticides (tonnes), and Average Temperature (°C) in the text fields.
        
    *   Select an Area (country) and Item (crop type) from the dropdowns.
        
    *   Click the "Predict" button.
        
4.  **View Results**The predicted yield (in hg/ha) will be displayed in a green section, along with the input values for Year, Average Rainfall, Pesticides, Average Temperature, Area, and Item.
    

Example Input and Output
------------------------

### Input

*   Year: 1990
    
*   Average Rainfall: 1485.0
    
*   Pesticides: 121.0
    
*   Average Temperature: 16.37
    
*   Area: Albania
    
*   Item: Maize
    

### Output

*   Predicted Yield: 36613.0 hg/ha
    
*   Details:
    
    *   Year: 1990
        
    *   Average Rainfall: 1485.0 mm/year
        
    *   Pesticides: 121.0 tonnes
        
    *   Average Temperature: 16.37 °C
        
    *   Area: Albania
        
    *   Item: Maize
        

Customization
-------------

*   **Model Updates**: Replace dtr.pkl and preprocessor.pkl with new models trained on updated data.
    
*   **Styling**: Modify the CSS in index.html to change colors, fonts, or layout.
    
*   **Data**: Update yield\_df.csv with new or additional crop yield data.
    

Troubleshooting
---------------

*   **Error: ModuleNotFoundError**Ensure all required packages are installed. Run pip install -r requirements.txt again.
    
*   **Flask Server Not Starting**Check if port 5000 is in use. Stop any other application using it or change the port in app.py by modifying app.run(debug=True) to app.run(debug=True, port=5001).
    
*   **Prediction Issues**Verify that dtr.pkl and preprocessor.pkl are compatible with the input data format. Ensure numerical inputs are valid (e.g., no letters).
    

Acknowledgements
----------------

*   Dataset inspiration from agricultural yield statistics.
    
*   Flask and scikit-learn communities for robust tools.
    
*   Design inspiration from modern web interfaces.
