from dash import html, dcc, Input, Output
from app import app
from components.layout import wrap_with_layout

# Define the aside (sidebar) content for the dashboard page
aside_content = html.Div([
    html.H4("Dashboard", className="md-text-primary", style={'margin-bottom': '20px'}),
    html.Div([
        html.H5("Tools", className="md-text-secondary", style={'margin-bottom': '12px'}),
        html.Ul([
            html.Li(html.A("📊 Analytics", href="#analytics", className="md-ripple")),
            html.Li(html.A("📈 Reports", href="#reports", className="md-ripple")),
            html.Li(html.A("⚙️ Settings", href="#settings", className="md-ripple")),
            html.Li(html.A("👤 Profile", href="#profile", className="md-ripple"))
        ]),
        
        html.Hr(),
        
        html.H5("Preferences", className="md-text-secondary", style={'margin-bottom': '12px'}),
        html.Div([
            html.Label("Theme:", className="md-text-secondary", 
                      style={'display': 'block', 'margin-bottom': '8px', 'font-size': '14px'}),
            dcc.Dropdown(
                id='theme-dropdown',
                options=[
                    {'label': 'Light', 'value': 'light'},
                    {'label': 'Dark', 'value': 'dark'}
                ],
                value='light',
                style={'margin-bottom': '16px', 'font-size': '14px'}
            ),
            
            html.Label("Notifications:", className="md-text-secondary", 
                      style={'display': 'block', 'margin-bottom': '8px', 'font-size': '14px'}),
            dcc.Checklist(
                id='notifications',
                options=[
                    {'label': 'Email alerts', 'value': 'email'},
                    {'label': 'Push notifications', 'value': 'push'}
                ],
                value=['email'],
                style={'font-size': '14px'}
            )
        ], className="md-card", style={'padding': '16px'})
    ])
])

# Define the main content for the dashboard page
main_content = html.Div([
    html.Div([
        html.H1("📊 Material Dashboard", className="md-text-primary"),
        html.P("Your modern analytics dashboard", className="md-text-secondary", 
               style={'font-size': '18px', 'margin-bottom': '32px'})
    ], className="md-card"),
    
    # Stats cards
    html.Div([
        html.Div([
            html.Div([
                html.H3("1,234", className="md-text-primary", style={'margin': '0', 'font-size': '2rem'}),
                html.P("Active Users", className="md-text-secondary", style={'margin': '8px 0 0 0'})
            ], style={'text-align': 'center'}),
            html.Div("📈", style={'font-size': '24px', 'position': 'absolute', 'top': '16px', 'right': '16px'})
        ], className="md-card md-elevation-2", style={'position': 'relative', 'margin': '8px'}),
        
        html.Div([
            html.Div([
                html.H3("98.5%", className="md-text-primary", style={'margin': '0', 'font-size': '2rem'}),
                html.P("Uptime", className="md-text-secondary", style={'margin': '8px 0 0 0'})
            ], style={'text-align': 'center'}),
            html.Div("⚡", style={'font-size': '24px', 'position': 'absolute', 'top': '16px', 'right': '16px'})
        ], className="md-card md-elevation-2", style={'position': 'relative', 'margin': '8px'}),
        
        html.Div([
            html.Div([
                html.H3("€12.4k", className="md-text-primary", style={'margin': '0', 'font-size': '2rem'}),
                html.P("Revenue", className="md-text-secondary", style={'margin': '8px 0 0 0'})
            ], style={'text-align': 'center'}),
            html.Div("💰", style={'font-size': '24px', 'position': 'absolute', 'top': '16px', 'right': '16px'})
        ], className="md-card md-elevation-2", style={'position': 'relative', 'margin': '8px'})
    ], style={'display': 'grid', 'grid-template-columns': 'repeat(auto-fit, minmax(200px, 1fr))', 'gap': '16px', 'margin-bottom': '24px'}),
    
    # Interactive section
    html.Div([
        html.H2("🔧 Interactive Demo", className="md-text-primary"),
        html.P("Try the Material Design input field below:", className="md-text-secondary"),
        dcc.Input(
            id='input-text', 
            type='text', 
            value='Type here',
            placeholder='Enter your message...',
            style={'width': '100%', 'margin-bottom': '16px'}
        ),
        html.Div(
            id='output-text',
            className="md-card md-elevation-1",
            style={'min-height': '60px', 'padding': '16px', 'font-family': 'monospace', 'background-color': 'var(--md-surface)'}
        )
    ], className="md-card"),
    
    # Floating Action Button
    html.Button("➕", className="md-fab", title="Add new item")
])

@app.callback(
    Output('output-text', 'children'),
    Input('input-text', 'value')
)
def update_text(value):
    return f"You typed: {value}"

# Create the layout using our layout wrapper
layout = wrap_with_layout(main_content, aside_content)
