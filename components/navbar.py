# components/navbar.py
from dash import html

navbar = html.Nav([
    html.Div([
        html.A("Home", href="/", style={
            'color': '#007bff',
            'text-decoration': 'none',
            'margin-right': '30px',
            'font-weight': '500',
            'padding': '10px 15px',
            'border-radius': '4px',
            'transition': 'background-color 0.3s'
        }),
        html.A("Dashboard", href="/dashboard", style={
            'color': '#007bff',
            'text-decoration': 'none',
            'font-weight': '500',
            'padding': '10px 15px',
            'border-radius': '4px',
            'transition': 'background-color 0.3s'
        })
    ], style={'display': 'flex', 'align-items': 'center'})
], style={
    'background-color': '#ffffff',
    'border-bottom': '1px solid #dee2e6',
    'padding': '15px 30px',
    'box-shadow': '0 2px 4px rgba(0,0,0,0.1)',
    'position': 'sticky',
    'top': '0',
    'z-index': '1000',
    'width': '100%',
    'box-sizing': 'border-box'
})
