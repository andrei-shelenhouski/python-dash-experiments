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
            html.H4("Sidebar", style={'margin-bottom': '20px'}),
            html.P("This is the sidebar area"),
            html.Hr(),
            html.P("Additional sidebar content can go here")
        ])
    
    # Default main content if none provided
    if main_content is None:
        main_content = html.Div([
            html.H2("Main Content Area"),
            html.P("This is the main content area")
        ])
    
    layout = html.Div([
        # Navbar at the top
        navbar,
        
        # Main container with aside and main content
        html.Div([
            # Aside (sidebar)
            html.Aside([
                aside_content
            ], style={
                'width': '250px',
                'min-height': 'calc(100vh - 60px)',  # Adjust based on navbar height
                'background-color': '#f8f9fa',
                'padding': '20px',
                'border-right': '1px solid #dee2e6',
                'box-sizing': 'border-box'
            }),
            
            # Main content area
            html.Main([
                main_content
            ], style={
                'flex': '1',
                'padding': '20px',
                'min-height': 'calc(100vh - 60px)',  # Adjust based on navbar height
                'box-sizing': 'border-box'
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
