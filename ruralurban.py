 # -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:09:52 2021

@author: mutuma
"""
# importing libraries
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import numpy
import plotly.express as px


project_data = pd.read_csv(r'C:/Users/mutuma/Documents/GIS/CV.Eric/python/rural_urban dashboard/Rural_Urban_Population_By_Age_Sex_and_by_District__2009.csv')


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1("RURAL URBAN POPULATION IN KENYA",
                        style={'textAlign':'center'}), width=12)
                                ]),
    
    dbc.Row([
        dbc.Col(html.H1('BAR CHARTS'), width=6)
        
         ]),
    
    dbc.Row([
              dbc.Col( dcc.Dropdown (id='bardrop',
                  options=[
            {'label': 'County', 'value': 'children'},
        ],
        multi=True,
        value="NAIROBI" )),
        
             dbc.Col(dcc.Graph(id='my_barchart',figure={},
                               config={'displayModeBar':False}))
          
                   ])
                     ,
    dbc.Row([
        dbc.Col(html.H1('LINE CHARTS'), width=6)
        
         ]),
     dbc.Row([
              dbc.Col( dcc.Dropdown ( id='linedrop',
                  options=[
            {'label': 'County', 'value': 'children'},
        ],
        multi=True,
        value="NAIROBI" )),
        
             dbc.Col(dcc.Graph(id='my_linechart', figure={},
                               config={'displayModeBar':False}))
          
                   ]),
      dbc.Row([
        dbc.Col(html.H1(' SCATTER PLOTS'), width=6)
        
         ]),
     dbc.Row([
              dbc.Col( dcc.Dropdown ( id='scatterdrop',
                  options=[
            {'label': 'County', 'value': 'children'},
        ],
        multi=True,
        value="NAIROBI" )),
        
             dbc.Col(dcc.Graph(id='my_scatterplot', figure={},
                               config={'displayModeBar':False}))
          
                   ])                
   
       ])
      

   
             
figure =px.bar(project_data, x = 'Age_years', y='Total', 
               title='Total Population To Age Groups', 
               labels= {'x':'age', 'y':'population'} )  

@app.callback( Output('my_barchart', 'figure'),
             Output('my_linechart', 'figure'),
             Output('my_scatterplot', 'figure'),
             input('bardrop', 'value'),
             input('linedrop', 'value'),
             input('scatterdrop', 'value'),
             )




if __name__ == '__main__':
    app.run_server(debug=False)