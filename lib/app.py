import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from datahandler import dummyDataHandler
import plotly.express as px
import numpy as np
from datetime import datetime
import traceback

'''
This is a prototype webapp for the CORD19 challenge on Kaggle
This involves a demo pandas dataframe, and sample visualisations
All data here is fictional!
'''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dh = dummyDataHandler()

def make_bubbleplot(dh):
    return px.scatter(dummyDataHandler().get_pivot(), x="publish_time_month", y="phase", color="tag", size='count',
                 hover_name="tag", title='Occurance of research tag per month per phase sized by #Occurances')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='COVID-19: Visual Research Exploration Tool'),

    html.Marquee('The data in this tool is fictional!', draggable='true'),
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[    
            dcc.Graph(
            id='phase-plot',
            figure=make_bubbleplot(dh)
    )]),
        dcc.Tab(label='Discover', children=[
            html.Div(id='selected-element'),
            dcc.Dropdown(
                id=f'dropdown-tag',
                options=[{'label': k, 'value':k} for k in dh.data.tag.unique() if not pd.isna(k)],
                multi=True,
                value=[k for k in dh.data.tag.unique()]
            ),
            dcc.Dropdown(
                id=f'dropdown-phase',
                options=[{'label': k, 'value':k} for k in dh.data.phase.unique()],
                multi=True,
                value=[k for k in dh.data.phase.unique()]
            ),

            # ADD FILTER BASED ON VIRUS TYPE
            dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=min(dh.data.publish_time),
                max_date_allowed=max(dh.data.publish_time),
                initial_visible_month=datetime(2020, 1, 1),
                start_date=datetime(2020, 1, 1),
                end_date = datetime(2020, 1, 31)
        ),
            dcc.Graph(
            id='discover-plot',
            figure=None,
        )
        ]
        )
    ]),
])

@app.callback(
    Output('selected-element', 'children'),
    [Input('discover-plot', 'clickData')]
    )
def show_point_data(data_dict):
    try:
        print(data_dict)
        sha = data_dict['points'][0]['customdata'][0]
        abstract = dh.data.loc[sha]['abstract']
        return f'{abstract}'
    except Exception as e:
        print(e)
        traceback.print_exc()
        return ''

@app.callback(
    Output('discover-plot', 'figure'),
    [Input('dropdown-tag', 'value'),
    Input('dropdown-phase', 'value'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
    ]
    )
def discover_plot(tag, phase, start, end):
    #TODO make y, x and hue interchangable
    #TODO filter on drug type
    try:
        start = datetime.strptime(start.split('T')[0], '%Y-%m-%d')
        end = datetime.strptime(end.split('T')[0], '%Y-%m-%d')
        df = dh.get_date_range_data(start, end)
        df = df[(df.tag.isin(tag)) & (df.phase.isin(phase))]
        df['count'] = 1
        df= df.reset_index()
        fig = px.bar(df, x='phase', y='count', color='tag', hover_data=['sha', 'publish_time_month'])
        return fig
    except Exception as e:
        print(e)
        print('failed...')
        return None

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)