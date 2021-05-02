from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from trivia.extensions import db 
from trivia.models import Category, Question

category = Blueprint('category', __name__)


@category.route('/categories', methods=['GET'])
def get_categories():

    page = request.args.get('page', 1, type=int)
    start = (page-1) * 10
    end = start + 10
    
    questions = Question.query.all()
    formatted_questions = [question.format() for question in questions]
    
    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]
    
    return jsonify({
          'success': True,
          'questions': formatted_questions[start:end],
          'total_questions': len(formatted_questions),
          'categories': formatted_categories,
          'current_category': None
      })