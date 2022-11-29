# -*- coding: utf-8 -*-

from dash import Dash, callback, dcc, html, dash_table, dcc
from dash.dependencies import Input, Output
import pandas as pd
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('data/data.csv')
df['year'] = df["Datetime"].str[:4]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    assets_folder ="static",
    assets_url_path="static"
)
application = app.server
app.title = "Test Title"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_list = [html.H1('H1 Test'),]
index_list.append(html.Br())
index_list.append(dcc.Link(f'URL Here', href=f'/link'))
    
index_page = html.Div(index_list)

def output_tw(pathname):
    df = pd.DataFrame()
    
    layout = [
        html.H3(children='H3 test'),
    ]
    layout.append(html.H3(children=f'append test'))

    layout.append(html.Div(html.Button('button', id='refresh', n_clicks=0), style={'width': 100}),)

    layout.append(html.Div(children=[dcc.Slider(id='slider', min=2002,max=2018,value=2018, marks={2002:'2002',2004:'2004',2006:'2006',2008:'2008',2010:'2010',2012:'2012',2014:'2014',2016:'2016',2018:'2018'})]),)

    layout.append(html.Div(children=[dcc.Graph(id='consumption', style={'height': 400})]),)
    
    return layout

@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname[1:] == 'link':
        layout = output_tw(pathname)
        return html.Div(layout)
    else:
        return index_page

@app.callback(
    [Output('consumption', 'figure')],
    [Input('refresh','n_clicks'),Input('slider','value')])
def update_layout(n_clicks,value1):
    fig_consumption = go.Figure()
    if n_clicks > 0:
        
        df_output = df.loc[df['year'] == str(value1)]
        
        fig_consumption.add_trace(go.Scatter(x=df_output["Datetime"], y=df_output["Consumption"], mode='lines', connectgaps=True))
        fig_consumption.update_layout(showlegend=False)
    return [fig_consumption]

if __name__ == '__main__':
    application.run_server(port=8080, debug=False)