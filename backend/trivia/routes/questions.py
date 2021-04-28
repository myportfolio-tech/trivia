from flask import Blueprint, render_template, request, redirect, url_for


question = Blueprint('question', __name__)


@question.route('/questions', methods=['GET'])
def get_questions():

    return """ 
    <h1>THESE ARE THE QUESTIONS</h1>"""

