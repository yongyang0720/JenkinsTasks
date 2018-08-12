#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    TestJobs
    ~~~~~~~~~~~~
    Unit Test for Jobs.py

"""

import sys
sys.path.append('../bin')
from Jobs import Jobs
import unittest
import jenkins
import logging.handlers
import logging.config

class TestJobs(unittest.TestCase):
    def setUp(self):
        self.server = jenkins.Jenkins ('http://localhost:8080', username='jenkins', password='jenkins')
        self.logger = logging.getLogger('TestJobs')
        self.logger.setLevel(logging.INFO)

    # Test get all tasks
    def test_get_all_tasks(self):
        self.assertEqual(Jobs.get_all_tasks(self),'sucessed')

    # test create the task: task
    def test_create_task(self):
        self.assertEqual(Jobs.create_task(self, 'task'), 'failed')

    # test get the task: task
    def test_get_task(self):
        self.assertEqual(Jobs.get_task(self, 'task'), 'sucessed')

    # test build the task: task
    def test_build_task(self):
        self.assertEqual(Jobs.build_task(self, 'task'), 'failed')

    # test enable the task: task
    def test_enable_task(self):
        self.assertEqual(Jobs.enable_task(self, 'task'), 'sucessed')

    # test delete the task: task
    def test_delete_task(self):
        self.assertEqual(Jobs.delete_task(self, 'taskd'), 'failed')

if __name__ == '__main__':
    unittest.main()

