from dash import Dash
app = Dash()

import dash_html_components as html
app.layout = html.Div([
    html.H1("you can write your header details here")
])


if __name__ == '__main__':
    app.run_server()

