#!/usr/bin/env python3

import os

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''<h1>The host for this page is {host}</h1>
                <h1>The appname for this page is {appname}</h1>
                <h1>The path for this page is {g.path}</h1>'''
    
    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5556)
