import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from trivia import create_app
from trivia.models import Question, Category
from trivia.extensions import db



## TEST UNIT SETUP

def setup_test_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()




class TriviaTestCase(unittest.TestCase):

    ## This Test Sets up the test app, database, and tables
    def setUp(self):

        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}@{}/{}".format('psqladmin:administrator','localhost:5432', self.database_name)
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

    ### Test that the Home Route is up and returns "Hello" ###
    def test_check_home_page_return(self):
        
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual('Hello', res.get_data(as_text=True))

    ### Test that Categories Return ###
    def test_route_categories(self):
        
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()