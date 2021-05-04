from flask import Blueprint, request, jsonify, abort
from trivia.extensions import db 
from trivia.models import Category, Question

quizz = Blueprint('quizz', __name__)


@quizz.route('/quizz', methods=['POST'])
def play_quizz():

    # data from previous question by category
    data = request.get_json()
    previous_questions = data.get('previous_questions', None)
    quiz_category = data.get('quiz_category')

    print(previous_questions)
    print(quiz_category)

    if not quiz_category:
        abort(422)


    return jsonify({
        'question': 
        {
        'id': 1,
        'question': 'This is a question',
        'answer': 'This is an answer', 
        'difficulty': 5,
        'category': 4
        }
})

    # try:


    #     # specific quiz_category is not selected
    #     if (quiz_category["type"]) == "click":
    #         selected = Question.query.filter(Question.id.notin_(
    #             previous_questions)).order_by(func.random()).limit(1).all()

    #     else:
    #         # quiz_category is specified
    #         selected = Question.query.filter(
    #             Question.category == quiz_category["id"]).filter(
    #             Question.id.notin_(previous_questions)).order_by(
    #                 func.random()).limit(1).all()

    #     # if a question is returned - format it
    #     if len(selected) != 0:
    #         selected_question = [
    #             question.format() for question in selected]

    #         # remove brackets from question
    #         question = selected_question[0]

    #         result = {
    #             'success': True,
    #             'question': question
    #         }
    #     else:
    #         result = {
    #             'success': True
    #         }
    #     return jsonify(result)

    # except Exception as e:
    #     print('\n'+'Error retrieving question: ', e)
    #     abort(422)
