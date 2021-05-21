import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from flask_cors import CORS

from .models import Question, Category
from .extensions import db
from .routes.questions import question
from .routes.categories import category
from .routes.search import search
from .routes.quizzes import quizz
from .routes.error_handlers import errors


QUESTIONS_PER_PAGE = 10

def create_app(config_file='settings.py'):
  # create and configure the app
  app = Flask(__name__)
  app.config.from_pyfile(config_file)
    
  db.init_app(app)
  
  CORS(app)
  cors = CORS(app, resources={r"/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):

      response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

  app.register_blueprint(question)
  app.register_blueprint(category)
  app.register_blueprint(search)
  app.register_blueprint(quizz)
  app.register_blueprint(errors)



####      IMPORTANT      ####

### ALL TODOS are completed uder the backend/trivia/routes folder ### 

### COMPLETED  ### 
  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions '''
  ### The endpoint is completed under routes/categories
  

### COMPLETED ###
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID.'''
  ### The endpoint is completed under routes/questions
  

### COMPLETED ###
  '''
  @TODO: 
  Create an endpoint to POST a new question'''
  ###   ### The endpoint is completed under routes/questions


### COMPLETED ### 
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  '''
  ### The endpoint is completed under routes/search


### COMPELETED ###
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category.'''
  ### The endpoint is completed under routes/categories


### COMPLETED ###
  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. '''
  ### The endpoint is completed under routes/quizzes


### COMPLETED ###
  '''
  @TODO: 
  Create error handlers for all expected errors '''
  ### The endpoint is completed under routes/error_handlers
  
  return app

app = create_app()

