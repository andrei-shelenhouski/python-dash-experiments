# index.py
from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
from pages import home, dashboard

# Main app layout - just the URL location and page content
# Each page now handles its own layout with navbar and sidebar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run(debug=True, port=8051)
