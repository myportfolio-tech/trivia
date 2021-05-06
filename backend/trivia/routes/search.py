from flask import Blueprint, request, jsonify, abort
from trivia.extensions import db 
from trivia.models import Category, Question

search = Blueprint('search', __name__)


@search.route('/questions/search', methods=['POST'])
def search_questions():


    page = request.args.get('page', 1, type=int)
    start = (page-1) * 10
    end = start + 10
    
    data = request.get_json(force=True)
    search_term = data.get('searchTerm')

    questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

    if len(questions) == 0:
        abort(404)

    formatted_questions = [question.format() for question in questions]


    

    
    return jsonify({
          'success': True,
          'questions': formatted_questions[start:end],
          'total_questions': len(formatted_questions),
          'current_category': None
      })