#from flask import Flask, jsonify, json, request, render_template, redirect

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# region FOR INTEGRATING WITH GENERAL FLASK APP
# app_flask = Flask(__name__)
# app_dash = dash.Dash(__name__, server=app_flask, url_base_pathname='/pathname/')
# @app_flask.route("/my_route/",methods=['POST'])
# def my_route():
#     print('Received POST request at /my_route/')
#     return 'Received POST request at /my_route/'

# @app_flask.route('/') 
# def render_main():
#     return redirect('/pathname/')

#endregion

app_dash = dash.Dash(__name__, url_base_pathname='/pathname/')

app_dash.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    #app_flask.run()
    app_dash.run_server(debug=True)