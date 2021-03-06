import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from trivia import create_app
from trivia.models import Question, Category
from trivia.extensions import db


# TEST UNIT SETUP

def setup_test_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class TriviaTestCase(unittest.TestCase):

    # This Test Sets up the test app, database, and tables
    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}@{}/{}".format(
            'psqladmin:administrator', 'localhost:5432', self.database_name)
        setup_test_db(self.app, self.database_path)

        self.test_text = "test"

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # Test that the Home Route is up and returns "Hello" #
    def test_check_home_page_return(self):

        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual('Hello', res.get_data(as_text=True))

    # Test that Categories Return ###
    def test_route_categories(self):

        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        # Test the result is dictionary with a single key, 'categories'
        self.assertTrue(data.get('categories'))
        self.assertEqual(len(data), 1)

    def test_route_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        # Test response dictionary keys
        self.assertTrue(data.get('categories'))
        self.assertEqual(data.get('current_category'), None)
        self.assertTrue(data.get('questions'))
        self.assertTrue(data.get('success'))
        self.assertTrue(data.get('total_questions'))

        # Test there is data in payload
        self.assertNotEqual(data.get('total_questions'), 0)
        self.assertNotEqual(len(data.get('questions')), 0)

    def test_route_search_questions(self):
        res = self.client().post(
            '/questions/search',
            json={
                "searchTerm": "the"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        # Test response dictionary
        self.assertNotEqual(len(data), 0)
        self.assertEqual(data.get('success'), True)
        self.assertEqual(data.get('current_category'), None)
        self.assertTrue(data.get('questions'))
        self.assertNotEqual(data.get('total_questions'), 0)

    def test_route_play_quizz(self):
        # We are using category 4
        # There are 4 questions with category 4 with ids [5, 9, 12, 23]

        request_data = {
            'previous_questions': [5, 23],
            'quiz_category': {
                'id': 4,
                'type': 'History'
            }
        }

        res = self.client().post('/quizz', json=request_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data.get('question'))

        # Ensure route doesn't return questions already played
        self.assertNotEqual(data['question']['id'], 5)
        self.assertNotEqual(data['question']['id'], 23)

        # Ensure questions are what's expected.
        self.assertIn(data['question']['id'], [9, 12])
        self.assertIn(data['question']['question'],
                      ["What boxer's original name is Cassius Clay?",
                       "Who invented Peanut Butter?"])

    def test_route_question_create(self):

        new_question = {
            'question': 'Test question from test_trivia',
            'answer': 'Answer to test question from test_trivia',
            'difficulty': 2,
            'category': '1'
        }

        res = self.client().post('/questions', json=new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_bad_request(self):

        # send request with bad page data, load response
        res = self.client().get('/categories/67/questions')
        resdata = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(resdata['error'], 400)
        self.assertEqual(resdata['message'], "Bad Request")
        self.assertEqual(resdata['success'], False)

    def test_404_bad_request(self):

        # send request with bad page data, load response
        res = self.client().get('/categories/67')
        resdata = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(resdata['error'], 404)
        self.assertEqual(resdata['message'], "Not Found")
        self.assertEqual(resdata['success'], False)

    def test_404_search_not_found(self):
        """Tests search questions failure 404"""

        # send post request with search term that should fail
        res = self.client().post('/questions/search',
                                 json={"searchTerm": 
                                 "this_is_a_very_long_search_term_to_fail"})
        resdata = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(resdata['error'], 404)
        self.assertEqual(resdata['message'], "Not Found")
        self.assertEqual(resdata['success'], False)
        # check response status code


if __name__ == "__main__":
    unittest.main()
