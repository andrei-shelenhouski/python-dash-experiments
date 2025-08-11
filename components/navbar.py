# components/navbar.py
from dash import html

navbar = html.Nav([
    html.Div([
        # App title/logo
        html.Div([
            html.Span("📱", style={'font-size': '24px', 'margin-right': '12px'}),
            html.Span("Material Dash", style={
                'font-size': '20px', 
                'font-weight': '500',
                'color': 'white'
            })
        ], style={
            'display': 'flex', 
            'align-items': 'center',
            'margin-right': '48px'
        }),
        
        # Navigation links
        html.Div([
            html.A("Home", href="/", className="md-ripple"),
            html.A("Dashboard", href="/dashboard", className="md-ripple")
        ], style={'display': 'flex', 'gap': '8px'})
    ], style={
        'display': 'flex', 
        'align-items': 'center', 
        'justify-content': 'space-between',
        'width': '100%'
    })
])
