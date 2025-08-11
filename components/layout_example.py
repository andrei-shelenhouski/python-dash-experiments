# components/layout_example.py
"""
Example of how to use the layout component

This file demonstrates different ways to use the layout component
in your Dash applications.
"""

from dash import html
from .layout import create_layout, wrap_with_layout

# Example 1: Using create_layout with custom aside and main content
def example_with_custom_content():
    aside_content = html.Div([
        html.H4("Custom Sidebar"),
        html.P("This is custom sidebar content"),
        html.Ul([
            html.Li("Item 1"),
            html.Li("Item 2"),
            html.Li("Item 3")
        ])
    ])
    
    main_content = html.Div([
        html.H1("Custom Main Content"),
        html.P("This is the main content area"),
        html.Div("Additional content goes here")
    ])
    
    return create_layout(aside_content, main_content)

# Example 2: Using wrap_with_layout to wrap existing content
def example_with_wrapped_content():
    existing_content = html.Div([
        html.H1("Existing Content"),
        html.P("This content was wrapped with the layout")
    ])
    
    return wrap_with_layout(existing_content)

# Example 3: Using default layout (no custom content)
def example_with_default_content():
    return create_layout()

# Example 4: Custom aside with default main content
def example_with_custom_aside():
    custom_aside = html.Div([
        html.H4("Navigation"),
        html.Nav([
            html.A("Link 1", href="#"),
            html.Br(),
            html.A("Link 2", href="#"),
            html.Br(),
            html.A("Link 3", href="#")
        ])
    ])
    
    return create_layout(aside_content=custom_aside)
