# -*- coding: utf-8 -*-

from dash import Dash, callback, dcc, html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import csv

application = Dash(__name__, suppress_callback_exceptions=True)
server = application.server
application.title = "Test Title"

application.layout = html.Div([
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
    
    return layout

@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname[1:] == 'link':
        layout = output_tw(pathname)
        return html.Div(layout)
    else:
        return index_page

if __name__ == '__main__':
    application.run_server(debug=False)
