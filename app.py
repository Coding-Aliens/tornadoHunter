import json
from random import random

from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
from bokeh.embed import components, json_item
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral11
from bokeh.transform import factor_cmap
from bokeh.palettes import Category20, Turbo256
from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.models import ColumnDataSource
from bokeh.resources import CDN
from bokeh.core import json_encoder
import numpy as np


app = Flask(__name__)
data = pd.read_csv('us_tornado_dataset_1950_2021.csv')
import pandas as pd
@app.route('/by_year')
def by_year():
    # Step 2.1: Load data from an XLSX file
    df = pd.read_excel('1995-2022.xlsx', engine='openpyxl')
    source = ColumnDataSource(df)
    p = figure(title="Yearly Data", x_axis_label='Year', y_axis_label='Number', sizing_mode="stretch_width", height=400)
    p.line(x='Year', y='Number', source=source, legend_label="Year vs. Number", line_width=2, line_color="black")
    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    return render_template('by_year.html', script1 = script1, div1 = div1, cdn_js =cdn_js)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tornado-data/<string:dataset_id>')
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

@app.route('/plot')
def plot_view():
    states = sorted(data['st'].unique())
    custom_palette = Category20[20] * 3
    custom_palette = custom_palette[:53]  # Ensure exactly 50 colors

    data_by_state = data.groupby('st').size().reset_index(name='counts')
    source = ColumnDataSource(data_by_state)

    p = figure(x_range=states, title="Occurrences by State", toolbar_location=None, tools="")
    p.vbar(x='st', top='counts', width=0.9, source=source,
           line_color='white', fill_color=factor_cmap('st', palette=custom_palette, factors=states))

    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = "State"
    p.yaxis.axis_label = "Number of Occurrences"
    p.xaxis.major_label_orientation = 1.2

    script, div = components(p)
    return render_template("plot_template.html", script=script, div=div, title="Occurrences Over States")

if __name__ == '__main__':
    app.run(debug=True)
