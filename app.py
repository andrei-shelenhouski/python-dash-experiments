# app.py
from dash import Dash

# External stylesheets for Material Design
external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap',
    'https://fonts.googleapis.com/icon?family=Material+Icons'
]

app = Dash(__name__, 
          suppress_callback_exceptions=True,
          external_stylesheets=external_stylesheets)
server = app.server  # for deploying to services like Heroku
