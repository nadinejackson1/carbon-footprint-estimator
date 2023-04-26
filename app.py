from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

data = {
    'Activity': ['Driving', 'Flying', 'Biking', 'Walking'],
    'CO2_Emission': [0.24, 0.15, 0.008, 0.001]
}
emissions_df = pd.DataFrame(data)

def estimate_carbon_footprint(activity, distance, people=1):
    emission = emissions_df.loc[emissions_df['Activity'] == activity, 'CO2_Emission'].values[0]
    carbon_footprint = emission * distance * people
    return carbon_footprint

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    activity = request.form["activity"]
    distance = float(request.form["distance"])
    people = int(request.form["people"])
    
    carbon_footprint = estimate_carbon_footprint(activity, distance, people)
    return jsonify(carbon_footprint=carbon_footprint)

if __name__ == "__main__":
    app.run(debug=True)
