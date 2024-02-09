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

@app.route('/tornado_data')
def tornado_data():
    # Create a Plotly figure
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', color='magnitude',
                         hover_name='location', size='magnitude',
                         projection="natural earth", title="Tornado Data")
    # Convert the figure to JSON
    graphJSON = json.dumps(fig, cls=pio.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)
