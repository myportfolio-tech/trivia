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
    def test_setUp(self):

        self.app = create_app(config_file='settings.py')
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        # postgresql://psqladmin:administrator@localhost:5432/trivia
        self.database_path = "postgresql://{}@{}/{}".format('psqladmin:administrator','localhost:5432', self.database_name)
        setup_test_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()