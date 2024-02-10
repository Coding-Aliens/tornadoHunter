from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__)

# Load the tornado data
df = pd.read_csv('tornado_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualization')
def visualization():
    # Create a Plotly figure
    fig = px.scatter_geo(df, lat='slat', lon='slon', color='mag',
                         hover_name='st', size='mag',
                         projection="natural earth",
                         title="Tornado Data", scope='north america')

    # Convert the figure to JSON
    graphJSON = pio.to_json(fig)
    return render_template('visualization.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
