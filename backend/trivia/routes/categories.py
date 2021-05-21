from flask import Blueprint, request, jsonify, abort
from trivia.extensions import db
from trivia.models import Category, Question

category = Blueprint('category', __name__)

# This Route is used for testing


@category.route('/')
def index():
    return "Hello"


@category.route('/categories', methods=['GET'])
def get_categories():

    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    categories = Category.query.all()

    categories_dict = {}
    for category in categories:
        categories_dict[category.id] = category.type

    return jsonify({
        'categories': categories_dict
    })


@category.route('/categories/<int:id>/questions', methods=['GET'])
def get_questions_per_category(id):

    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    category = Category.query.filter_by(id=id).one_or_none()

    if category is None:
        abort(400)

    questions = Question.query.filter_by(category=category.id).all()
    formatted_questions = [question.format() for question in questions]

    return jsonify({
        'questions': formatted_questions[start:end],
        'total_questions': len(formatted_questions),
        'currentCategory': category.type
    })
