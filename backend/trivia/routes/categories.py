from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from trivia.extensions import db 
from trivia.models import Category, Question

category = Blueprint('category', __name__)


@category.route('/categories', methods=['GET'])
def get_categories():

    page = request.args.get('page', 1, type=int)
    start = (page-1) * 10
    end = start + 10

    categories_dict = {}
    for category in categories:
        categories_dict[category.id] = category.type
    
    return jsonify({
          'categories': categories_dict
      })