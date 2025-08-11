# components/layout.py
from dash import html
from .navbar import navbar

def create_layout(aside_content=None, main_content=None):
    """
    Create a layout with navbar on top and aside/main content below
    
    Args:
        aside_content: Content for the aside section (sidebar)
        main_content: Content for the main section
    """
    
    # Default aside content if none provided
    if aside_content is None:
        aside_content = html.Div([
            html.H4("Navigation", className="md-text-primary"),
            html.Hr(),
            html.Div([
                html.P("Quick links", className="md-text-secondary", style={'margin-bottom': '12px'}),
                html.Ul([
                    html.Li(html.A("Getting Started", href="#start", className="md-ripple")),
                    html.Li(html.A("Documentation", href="#docs", className="md-ripple")),
                    html.Li(html.A("Settings", href="#settings", className="md-ripple"))
                ])
            ])
        ])
    
    # Default main content if none provided
    if main_content is None:
        main_content = html.Div([
            html.H1("Welcome", className="md-text-primary"),
            html.P("This is your Material Design Dash application", className="md-text-secondary"),
            html.Div([
                html.Button("Get Started", className="md-ripple"),
                html.Button("Learn More", className="md-button-outlined md-ripple", style={'margin-left': '12px'})
            ], style={'margin-top': '24px'})
        ], className="md-card")
    
    layout = html.Div([
        # Navbar at the top
        navbar,
        
        # Main container with aside and main content
        html.Div([
            # Aside (sidebar)
            html.Aside([
                aside_content
            ], style={
                'width': '280px',
                'min-height': 'calc(100vh - 64px)',  # Adjust based on navbar height
                'padding': '24px',
                'box-sizing': 'border-box'
            }),
            
            # Main content area
            html.Main([
                main_content
            ], style={
                'flex': '1',
                'padding': '24px',
                'min-height': 'calc(100vh - 64px)',  # Adjust based on navbar height
                'box-sizing': 'border-box',
                'background-color': 'var(--md-background)'
            })
        ], style={
            'display': 'flex',
            'width': '100%'
        })
    ], style={
        'margin': '0',
        'padding': '0',
        'font-family': 'Arial, sans-serif'
    })
    
    return layout

# Alternative: Create a simple layout wrapper for existing content
def wrap_with_layout(content, aside_content=None):
    """
    Wrap existing content with the layout structure
    
    Args:
        content: The main content to wrap
        aside_content: Optional aside content
    """
    return create_layout(aside_content=aside_content, main_content=content)
