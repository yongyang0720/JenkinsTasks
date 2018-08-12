#!/usr/bin/env python3
 # -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('../bin')
import flask

class TesJobs(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask(__name__)
        self.client = self.app.test_client()

    def test_app( self ):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/tasks')
        self.assertEqual(response.status_code, 404)

        response = self.client.delete('/tasks')
        self.assertEqual(response.status_code, 404)

        response = self.client.put('/tasks')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()