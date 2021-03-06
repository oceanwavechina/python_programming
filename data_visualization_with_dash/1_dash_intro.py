'''
Created on Dec 15, 2018

@author: liuyanan
'''

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Dash Tutorialssss'),
    dcc.Graph(id='example', figure={
        'data': [
            {'x': [1, 2, 3, 4, 5], 'y':[5, 6, 7, 2, 3, 1], 'type':'line', 'name':'boats'},
            {'x': [1, 2, 3, 4, 5], 'y':[7, 8, 9, 10, 5, 3], 'type':'bar', 'name':'cars'},
        ],
        'layout':{
            'title': 'Basic Dash Exampple'
        }
    })
])


if __name__ == '__main__':
    app.run_server(debug=True)
