#~/movie-bag/tests/test_signup.py

import unittest
import json

from moviebag import create_app
from moviebag.database.db import db

# def test_register(client, app):

#     with app.app_context():
#         app = test_client()
#         self.db = db.get_db()

# class SignupTest(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.db = db.get_db()

#     def test_successful_signup(self):
#         # Given
#         payload = json.dumps({
#             "email": "paurakh011@gmail.com",
#             "password": "mycoolpassword"
#         })

#         # When
#         response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

#         # Then
#         self.assertEqual(str, type(response.json['id']))
#         self.assertEqual(200, response.status_code)

#     def tearDown(self):
#         # Delete Database collections after the test is complete
#         for collection in self.db.list_collection_names():
#             self.db.drop_collection(collection)
