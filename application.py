from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the CSV file into the 'car' DataFrame
car = pd.read_csv("Cleaned Car.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(),reverse=True)
    fuel_type = car['fuel_type'].unique()  # No need to sort unique values
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_type=fuel_type)

if __name__ == "__main__":
    app.run(debug=True)
