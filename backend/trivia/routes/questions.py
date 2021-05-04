from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from trivia.extensions import db 
from trivia.models import Category, Question

question = Blueprint('question', __name__)


@question.route('/questions', methods=['GET'])
def get_questions():

    page = request.args.get('page', 1, type=int)
    start = (page-1) * 10
    end = start + 10
    
    questions = Question.query.all()
    formatted_questions = [question.format() for question in questions]
    
    categories = Category.query.all()
    categories_dict = {}
    for category in categories:
        categories_dict[category.id] = category.type
    

    
    return jsonify({
          'success': True,
          'questions': formatted_questions[start:end],
          'total_questions': len(formatted_questions),
          'categories': categories_dict,
          'current_category': None
      })


@question.route('/questions', methods=['POST'])
def add_questions():

    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')
    difficulty = data.get('difficulty')
    category = data.get('category')

    new_question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
    new_question.insert()

    return jsonify ({
        'success': True
    })


@question.route('/questions/<int:question_id>/delete', methods=['DELETE'])
def search_questions(question_id):

    question = Question.query.get_or_404(question_id)
    question.delete()

    return jsonify ({
        'success': True
    })

