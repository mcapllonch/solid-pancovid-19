import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datahandler import dummyDataHandler
import plotly.express as px
import numpy as np
'''
This is a prototype webapp for the CORD19 challenge on Kaggle
This involves a demo pandas dataframe, and sample visualisations
All data here is fictional!
'''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='COVID-19: Visual Research Exploration Tool'),

    html.Marquee('The data in this tool is fictional!', draggable='true'),

    dcc.Graph(
        id='phase-plot',
        figure=px.scatter(dummyDataHandler().get_pivot(), x="publish_time", y="phase",
         size="count", color="tag",
                 hover_name="tag", hover_data=['count'], title='Occurance of research tag per month per phase sized by #Occurances')
    )
])



if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)