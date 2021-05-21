from flask import Blueprint, request, jsonify, abort
from trivia.extensions import db
import random
from trivia.models import Category, Question
from sqlalchemy import func

quizz = Blueprint('quizz', __name__)


def pick_next_question(questions, previous_questions):

    for q in questions:
        if q.id not in previous_questions:

            return q

    return False


@quizz.route('/quizz', methods=['POST'])
def play_quizz():

    # data from previous question by category
    data = request.get_json()
    previous_questions = data.get('previous_questions', None)
    quiz_category = data.get('quiz_category')

    print(data)
    print('PREVIOUS QUESTIONS:', previous_questions)
    print('QUIZ CATEGORY:', quiz_category)

    if not quiz_category:
        abort(422)

    category = Category.query.filter_by(type=quiz_category.get('type')).first()

    if quiz_category.get('type') == "click":
        questions = Question.query.order_by(func.random()).all()
    else:
        questions = Question.query.filter_by(
            category=str(category.id)).order_by(
            func.random()).all()

    question = pick_next_question(questions, previous_questions)
    if question:

        return jsonify({
            'question':
            {
                'id': question.id,
                'question': question.question,
                'answer': question.answer,
                'difficulty': question.difficulty,
                'category': question.category
            }
        })

    else:

        return jsonify({
            'question': None
        })
