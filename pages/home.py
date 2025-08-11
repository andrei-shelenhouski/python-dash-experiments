from dash import html
from components.layout import wrap_with_layout

# Define the aside (sidebar) content for the home page
aside_content = html.Div([
    html.H4("Home", className="md-text-primary", style={'margin-bottom': '20px'}),
    html.Ul([
        html.Li(html.A("🚀 Getting Started", href="#getting-started", className="md-ripple")),
        html.Li(html.A("✨ Features", href="#features", className="md-ripple")),
        html.Li(html.A("📚 Documentation", href="#docs", className="md-ripple")),
        html.Li(html.A("🔧 Settings", href="#settings", className="md-ripple"))
    ]),
    html.Hr(),
    html.Div([
        html.H5("Quick Stats", className="md-text-secondary"),
        html.Div([
            html.Div([
                html.H4("2", className="md-text-primary", style={'margin': '0', 'font-size': '24px'}),
                html.P("Pages", className="md-text-secondary", style={'margin': '4px 0', 'font-size': '12px'})
            ], className="md-card", style={'text-align': 'center', 'padding': '16px', 'margin': '8px 0'}),
            html.Div([
                html.H4("5", className="md-text-primary", style={'margin': '0', 'font-size': '24px'}),
                html.P("Components", className="md-text-secondary", style={'margin': '4px 0', 'font-size': '12px'})
            ], className="md-card", style={'text-align': 'center', 'padding': '16px', 'margin': '8px 0'})
        ])
    ])
])

# Define the main content for the home page
main_content = html.Div([
    html.Div([
        html.H1("🏠 Welcome Home", className="md-text-primary"),
        html.P("Experience Material Design in your Dash application", 
               className="md-text-secondary", 
               style={'font-size': '18px', 'margin-bottom': '32px'}),
        
        # Hero actions
        html.Div([
            html.Button("Explore Dashboard", className="md-ripple", id="dashboard-btn"),
            html.Button("Learn More", className="md-button-outlined md-ripple", 
                       style={'margin-left': '12px'})
        ], style={'margin-bottom': '48px'})
    ], className="md-card"),
    
    html.Div([
        html.H2("🚀 Getting Started", id="getting-started", className="md-text-primary"),
        html.P("This Material Design Dash application features:", className="md-text-secondary"),
        html.Ul([
            html.Li("🎨 Material Design 3 color system and typography"),
            html.Li("📱 Responsive layout with mobile-first approach"),
            html.Li("🔄 Smooth animations and transitions"),
            html.Li("♿ Accessibility-focused components"),
            html.Li("🎯 Touch-friendly interactive elements")
        ], style={'line-height': '1.8'})
    ], className="md-card"),
    
    html.Div([
        html.H2("✨ Key Features", id="features", className="md-text-primary"),
        html.Div([
            html.Div([
                html.H3("🎨 Material Colors", className="md-text-primary"),
                html.P("Consistent color palette following Material Design guidelines", 
                       className="md-text-secondary")
            ], className="md-card", style={'margin': '12px 0'}),
            
            html.Div([
                html.H3("📐 Elevation System", className="md-text-primary"),
                html.P("Proper shadows and depth to create visual hierarchy", 
                       className="md-text-secondary")
            ], className="md-card md-elevation-4", style={'margin': '12px 0'}),
            
            html.Div([
                html.H3("🔄 Ripple Effects", className="md-text-primary"),
                html.P("Interactive feedback on buttons and clickable elements", 
                       className="md-text-secondary")
            ], className="md-card md-elevation-8", style={'margin': '12px 0'})
        ])
    ])
])

# Create the layout using our layout wrapper
layout = wrap_with_layout(main_content, aside_content)
