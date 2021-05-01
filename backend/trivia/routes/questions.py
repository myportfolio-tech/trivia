from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from trivia.extensions import db 
from trivia.models import Question

question = Blueprint('question', __name__)


@question.route('/questions', methods=['GET'])
def get_questions():

    questions = Question.query.all()
    
    return jsonify(questions)
