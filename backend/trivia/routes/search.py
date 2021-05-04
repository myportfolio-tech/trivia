from flask import Blueprint, request, jsonify, abort
from trivia.extensions import db 
from trivia.models import Category, Question

search = Blueprint('search', __name__)