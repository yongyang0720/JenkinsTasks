#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    App
    ~~~~~~~~~~~~
    Web Service and API

"""

import flask
import Jobs
from flask import make_response,jsonify,request

app = flask.Flask(__name__)
tasks = Jobs.Jobs()

# Get the task
@app.route ('/v1/<task_name>', methods=['GET'])
def api_get_task(task_name):
    response = tasks.get_task(task_name)
    if response['Error Code'] == '0':
        return make_response(jsonify(response),200)
    else:
        return make_response(jsonify(response),int(response['Error Code']))

# create the task
@app.route ('/v1/<task_name>', methods=['POST'])
def api_create_task(task_name):
    response = tasks.create_task(task_name)
    if response['Error Code'] == '0':
        return make_response(jsonify(response),200)
    else:
        return make_response(jsonify(response),int(response['Error Code']))

# Build the task
@app.route ('/v1/<task_name>', methods=['PUT'])
def api_build_task(task_name):
    if request.form['action']=='build':
        response = tasks.build_task(task_name)
        if response['Error Code'] == '0':
            return make_response (jsonify (response), 200)
        else:
            return make_response (jsonify (response), int(response['Error Code']))

# Enable the task
    elif request.form['action'] == 'enable':
        response = tasks.enable_task(task_name)
        if response['Error Code'] == '0':
            return make_response (jsonify (response), 200)
        else:
            return make_response (jsonify (response), int(response['Error Code']))

# Delete the task
@app.route('/v1/<task_name>', methods=['DELETE'])
def api_delete_task(task_name):
    response = tasks.delete_task(task_name)
    if response['Error Code'] == '0':
        return make_response(jsonify(response),200)
    else:
        return make_response(jsonify(response),int(response['Error Code']))
