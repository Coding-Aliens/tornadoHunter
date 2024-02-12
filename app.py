from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:dataset_id>')
def show_dataset(dataset_id):
    # Logic to load the appropriate dataset based on dataset_id
    # For example, '05-07_torn' could be mapped to a specific file or database query
    data_file = f"killer-tornado-data/{dataset_id}.csv"  # Construct file name dynamically
    df = pd.read_csv(data_file)
    fig = px.scatter_geo(df, lat='slat', lon='slon', scope='usa',
                         color='mag', size='mag',
                         title=f"Tornadoes Dataset: {dataset_id}")
    graphJSON = pio.to_json(fig)
    return render_template('visualization.html', dataset_id=dataset_id, graphJSON=graphJSON)

@app.route('/navigation')
def navigation():
    return render_template('navigation.html')

if __name__ == '__main__':
    app.run(debug=True)
