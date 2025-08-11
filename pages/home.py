from dash import html
from components.layout import wrap_with_layout

# Define the aside (sidebar) content for the home page
aside_content = html.Div([
    html.H4("Home Navigation", style={'color': '#495057', 'margin-bottom': '20px'}),
    html.Ul([
        html.Li(html.A("Getting Started", href="#getting-started", style={'color': '#007bff', 'text-decoration': 'none'})),
        html.Li(html.A("Features", href="#features", style={'color': '#007bff', 'text-decoration': 'none'})),
        html.Li(html.A("Documentation", href="#docs", style={'color': '#007bff', 'text-decoration': 'none'}))
    ], style={'list-style-type': 'none', 'padding': '0'}),
    html.Hr(style={'margin': '20px 0'}),
    html.Div([
        html.H5("Quick Stats", style={'color': '#495057'}),
        html.P("Pages: 2", style={'margin': '5px 0'}),
        html.P("Components: 3", style={'margin': '5px 0'})
    ])
])

# Define the main content for the home page
main_content = html.Div([
    html.H1("🏠 Home Page", style={'color': '#212529', 'margin-bottom': '30px'}),
    html.P("Welcome to your Dash app — Angular style!", style={'font-size': '18px', 'margin-bottom': '30px'}),
    
    html.Div([
        html.H3("Getting Started", id="getting-started", style={'color': '#495057', 'margin-bottom': '15px'}),
        html.P("This is a multi-page Dash application with a clean layout structure. The layout includes:"),
        html.Ul([
            html.Li("A sticky navigation bar at the top"),
            html.Li("A sidebar for additional navigation and information"),
            html.Li("A main content area for your primary content")
        ]),
        
        html.H3("Features", id="features", style={'color': '#495057', 'margin': '30px 0 15px 0'}),
        html.P("Key features of this layout:"),
        html.Ul([
            html.Li("Responsive design with flexbox layout"),
            html.Li("Clean, modern styling"),
            html.Li("Sticky navigation for easy access"),
            html.Li("Reusable layout components")
        ]),
        
        html.Div([
            html.Button("Go to Dashboard", 
                       id="dashboard-btn",
                       style={
                           'background-color': '#007bff',
                           'color': 'white',
                           'border': 'none',
                           'padding': '12px 24px',
                           'border-radius': '4px',
                           'cursor': 'pointer',
                           'font-size': '16px',
                           'margin-top': '20px'
                       })
        ])
    ])
])

# Create the layout using our layout wrapper
layout = wrap_with_layout(main_content, aside_content)
