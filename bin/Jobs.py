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
            result = {
                'Task': 'Get All the  tasks',
                'Job Name': "Get all tasks",
                'Result': 'Successed',
                'Error Code': '0',
                'Description': 'Get all the task %s'
            }
            self.logger.info (resp)
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            result = {
                'Task': 'Get the task',
                'Job Name': task_name,
                'Result': 'Failed',
                'Error Code': '400',
                'Description': str(e)
            }
        self.logger.info(result)
        return resp

    # Get the task: task_name

    def get_task(self, task_name):
        try:
            jobs = self.server.get_job_info(task_name)
            resp = json.dumps(jobs)
            self.logger.info(resp)
            result = {
                'Task': 'Get the task',
                'Job Name': task_name,
                'Result' : 'Successed',
                'Error Code': '0',
                'Description': 'Get the tasks %s'%(task_name)
            }
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            result = {
                'Task': 'Get the task',
                'Job Name': task_name,
                'Result': 'Failed',
                'Error Code': '404',
                'Description': str (e)
            }

        self.logger.info(result)
        return result

    # Create the task: task_name

    def create_task(self, task_name):
        try:
            jobs = self.server.create_job(task_name,jenkins.EMPTY_CONFIG_XML)
            resp = json.dumps (jobs)
            self.logger.info(resp)
            result = {
                'Task': 'Create the task',
                'Job Name': task_name,
                'Result' : 'Successed',
                'Error Code': '0',
                'Description': 'Create the task %s'%(task_name)
            }
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            result = {
                'Task': 'Create the task',
                'Job Name': task_name,
                'Result': 'Failed',
                'Error Code': '400',
                'Description': str (e)
            }

        self.logger.info(result)
        return result


    def build_task(self, task_name):

        # Build the task: task_name
        try:
            jobs = self.server.build_job(task_name)
            resp = json.dumps(jobs)
            result = {
                'Task': 'Build the task',
                'Job Name': task_name,
                'Result' : 'Successed',
                'Error Code': '0',
                'Description': 'Get all the task %s'%(task_name)
            }
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            result = {
                'Task': 'Build the task',
                'Job Name': task_name,
                'Result': 'Failed',
                'Error Code': '400',
                'Description': str (e)
            }
        self.logger.info(result)
        return result

    def enable_task( self, task_name ):
        # Enable the task: task_name
        try:
            jobs = self.server.enable_job(task_name)
            resp = json.dumps(jobs)
            self.logger.info(resp)
            result = {
                'Task': 'Enable the task',
                'Job Name': task_name,
                'Result' : 'Successed',
                'Error Code': '0',
                'Description': 'Get all the task %s'%(task_name)
            }
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            result = {
                'Task': 'Enable the task',
                'Job Name': task_name,
                'Result': 'Failed',
                'Error Code': '400',
                'Description': str (e)
            }

        self.logger.info(resp)
        return result


    # Delete the task: task_name
    def delete_task(self,task_name):
        try:
            jobs = self.server.delete_job(task_name)
            resp = json.dumps(jobs)
            self.logger.info(resp)
            result = {
                'Task': 'Delete the task',
                'Job Name': task_name,
                'Result' : 'Successed',
                'Error Code': '0',
                'Description': 'Get all the task %s'%(task_name)
            }
        except jenkins.JenkinsException as e:
            self.logger.exception(e)
            result = {
                'Task': 'Delete the task',
                'Job Name': task_name,
                'Result': 'Failed',
                'Error Code': '404',
                'Description': str (e)
            }

        self.logger.info(result)
        return result