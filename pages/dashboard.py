from dash import html, dcc, Input, Output
from app import app
from components.layout import wrap_with_layout

# Define the aside (sidebar) content for the dashboard page
aside_content = html.Div([
    html.H4("Dashboard Tools", style={'color': '#495057', 'margin-bottom': '20px'}),
    html.Div([
        html.H5("Widgets", style={'color': '#6c757d', 'margin-bottom': '10px'}),
        html.Ul([
            html.Li("Text Input"),
            html.Li("Charts (coming soon)"),
            html.Li("Tables (coming soon)")
        ], style={'list-style-type': 'none', 'padding': '0', 'margin-bottom': '20px'}),
        
        html.H5("Settings", style={'color': '#6c757d', 'margin-bottom': '10px'}),
        html.Div([
            html.Label("Theme:", style={'display': 'block', 'margin-bottom': '5px'}),
            dcc.Dropdown(
                id='theme-dropdown',
                options=[
                    {'label': 'Light', 'value': 'light'},
                    {'label': 'Dark', 'value': 'dark'}
                ],
                value='light',
                style={'margin-bottom': '15px'}
            ),
            
            html.Label("Auto-refresh:", style={'display': 'block', 'margin-bottom': '5px'}),
            dcc.Checklist(
                id='auto-refresh',
                options=[{'label': 'Enable', 'value': 'enabled'}],
                value=[]
            )
        ])
    ])
])

# Define the main content for the dashboard page
main_content = html.Div([
    html.H1("📊 Dashboard", style={'color': '#212529', 'margin-bottom': '30px'}),
    
    html.Div([
        html.Div([
            html.H3("Interactive Text Input", style={'color': '#495057', 'margin-bottom': '15px'}),
            html.P("Type something in the input below to see real-time updates:"),
            dcc.Input(
                id='input-text', 
                type='text', 
                value='Type here',
                placeholder='Enter your text...',
                style={
                    'width': '100%',
                    'padding': '12px',
                    'border': '1px solid #ced4da',
                    'border-radius': '4px',
                    'font-size': '16px',
                    'margin-bottom': '20px'
                }
            ),
            html.Div(
                id='output-text',
                style={
                    'padding': '15px',
                    'background-color': '#f8f9fa',
                    'border': '1px solid #e9ecef',
                    'border-radius': '4px',
                    'min-height': '50px',
                    'font-family': 'monospace'
                }
            )
        ], style={
            'background-color': 'white',
            'padding': '30px',
            'border-radius': '8px',
            'box-shadow': '0 2px 4px rgba(0,0,0,0.1)',
            'margin-bottom': '30px'
        }),
        
        html.Div([
            html.H3("Quick Stats", style={'color': '#495057', 'margin-bottom': '15px'}),
            html.Div([
                html.Div([
                    html.H4("42", style={'color': '#007bff', 'margin': '0'}),
                    html.P("Active Users", style={'margin': '5px 0 0 0', 'color': '#6c757d'})
                ], style={
                    'text-align': 'center',
                    'padding': '20px',
                    'background-color': '#f8f9fa',
                    'border-radius': '4px',
                    'flex': '1',
                    'margin-right': '15px'
                }),
                html.Div([
                    html.H4("1,234", style={'color': '#28a745', 'margin': '0'}),
                    html.P("Total Visits", style={'margin': '5px 0 0 0', 'color': '#6c757d'})
                ], style={
                    'text-align': 'center',
                    'padding': '20px',
                    'background-color': '#f8f9fa',
                    'border-radius': '4px',
                    'flex': '1',
                    'margin-right': '15px'
                }),
                html.Div([
                    html.H4("98%", style={'color': '#ffc107', 'margin': '0'}),
                    html.P("Uptime", style={'margin': '5px 0 0 0', 'color': '#6c757d'})
                ], style={
                    'text-align': 'center',
                    'padding': '20px',
                    'background-color': '#f8f9fa',
                    'border-radius': '4px',
                    'flex': '1'
                })
            ], style={'display': 'flex'})
        ], style={
            'background-color': 'white',
            'padding': '30px',
            'border-radius': '8px',
            'box-shadow': '0 2px 4px rgba(0,0,0,0.1)'
        })
    ])
])

@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def update_text(value):
    return f"You typed: {value}"

# Create the layout using our layout wrapper
layout = wrap_with_layout(main_content, aside_content)
