from flask import Flask, request, render_template
import numpy as np
import pickle
import pandas as pd

# Loading models
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Load dataset to get unique values
df = pd.read_csv('yield_df.csv')
unique_areas = sorted(df['Area'].unique())
unique_items = sorted(df['Item'].unique())
unique_years = sorted(df['Year'].unique())

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', areas=unique_areas, items=unique_items, years=unique_years)

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        area = request.form['Area']
        item = request.form['Item']

        features = np.array([[year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, area, item]], dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features).reshape(1, -1)

        return render_template('index.html', 
                              prediction=prediction[0][0],
                              areas=unique_areas,
                              items=unique_items,
                              years=unique_years,
                              input_year=year,
                              input_rainfall=average_rain_fall_mm_per_year,
                              input_pesticides=pesticides_tonnes,
                              input_temp=avg_temp,
                              input_area=area,
                              input_item=item)

if __name__ == "__main__":
    app.run(debug=True)