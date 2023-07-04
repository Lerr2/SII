# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:51:43 2023

@author: Wei Lerr Wong
"""

# Import packages
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output



# load data
df = pd.read_csv('Greenhouse and energy information by registered corporation 2021-22.csv')
# make plot
fig = px.histogram(df, x='Net energy consumed (GJ)')

# initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

# set app layout
app.layout = html.Div(children=[
    html.H1('Energy Consumption', style={'textAlign':'center'}),
    html.Br(),
    dcc.Dropdown(
        options=[{'label': i, 'value': i} for i in df.columns],
        value='Net energy consumed (GJ)',
        id='dropdown',
        style={"width": "50%", "offset":1,},
        clearable=False,
    ),
    dcc.Graph(id='histogram', figure=fig)
])

# callbacks
@app.callback(
    Output(component_id='histogram', component_property='figure'),
    Input(component_id='dropdown', component_property='value'),
)
def update_hist(feature):
    fig = px.histogram(df, x=feature)
    return fig


# descriptive statistics 
df.describe()
#df2=df.groupby('Identifying details').agg({'Net energy consumed (GJ)':['mean'],
# 'Total scope 1 emissions (t CO2-e)':'mean',
# 'Total scope 2 emissions (t CO2-e)':'min',
# })




if __name__ == "__main__":
    app.run_server(debug=True)
    

