#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Jobs
    ~~~~~~~~~~~~
    Manage the Jobs

"""


import configparser
import logging.config
from flask import jsonify,json
import jenkins
import logging.handlers

class Jobs:

    def __init__(self):

        # load logger configuration
        try:
            log_config = "../conf/logging.conf"
            logging.config.fileConfig(log_config)
            self.logger = logging.getLogger ('normal')
        except Exception as e:
            print (e)
            self.logger = logging.getLogger('normal')
            self.logger = logging.FileHandler('../log/task.log', 'a')
            self.logger.setLevel(logging.INFO)
            print ('Use default configuration')

        # Get the configuration
        self.config = configparser.ConfigParser()

        try:
            self.config.read('../conf/App.ini')
        except FileNotFoundError as e:
            self.logger.exception(e)

        # Init jenkins server
        try:
            jenkins_server_url = self.config.get('jenkins_server', 'server_url')
            user_id = self.config.get('jenkins_server', 'username')
            api_token = self.config.get('jenkins_server', 'password')
            self.server = jenkins.Jenkins (jenkins_server_url, username=user_id, password=api_token)

        except Exception as e:
            print (e)
            self.server = jenkins.Jenkins ('http://localhost:8080', username='jenkins', password='jenkins')

    # Get all the tasks
    def get_all_tasks(self):
        try:
            jobs = self.server.get_jobs()
            if len(jobs):
                resp = json.dumps(jobs)
            else:
                resp = jsonify({'information': 'There is no job'})
            result = 'successed'
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            resp = jsonify({'error': 'Get jobs failed. Please check the logs for detals'})
            result = 'failed'
        self.logger.info(resp)
        return resp

    # Get the task: task_name

    def get_task(self, task_name):
        try:
            jobs = self.server.get_job_info(task_name)
            resp = json.dumps (jobs)
            result = 'sucessed'
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            resp = jsonify({'job': task_name, 'error': 'Get the job failed'})
            result = 'failed'

        self.logger.info(resp)
        return result

    # Create the task: task_name

    def create_task(self, task_name):
        try:
            jobs = self.server.create_job(task_name,jenkins.EMPTY_CONFIG_XML)
            resp = jsonify ({'job': task_name, 'information': 'Create the job  successed'})
            result = 'sucessed'
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            resp = jsonify({'job': task_name, 'error': 'Create the job failed, Please check the logs for detals'})
            result = 'failed'
        self.logger.info(resp)
        return result


    def build_task(self, task_name):

        # Build the task: task_name
        try:
            jobs = self.server.build_job(task_name)
            resp = json.dumps(jobs)
            result = 'sucessed'
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            resp = jsonify({'job': task_name, 'error': 'Build the job failed, Please check the logs for detals'})
            result = 'failed'
        self.logger.info(resp)
        return result

    def enable_task( self, task_name ):
        # Enable the task: task_name
        try:
            jobs = self.server.enable_job(task_name)
            resp = json.dumps(jobs)
            result = 'sucessed'
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            resp = jsonify({'job': task_name, 'error': 'Retrieve the job failed, Please check the logs for detals'})
            result = 'failed'

        self.logger.info(resp)
        return result


    # Delete the task: task_name
    def delete_task(self,task_name):
        try:
            jobs = self.server.delete_job(task_name)
            resp = jsonify ({'task': task_name, 'information': 'Delete the job successed'})
            result = 'succesed'
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            resp = jsonify({'job': task_name, 'error': 'Delete the job failed'})
            result = 'failed'

        self.logger.info(resp)
        return resp