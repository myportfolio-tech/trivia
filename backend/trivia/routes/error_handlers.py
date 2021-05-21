from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(400)
def error_400(error):
    
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400



@errors.app_errorhandler(404)
def error_404(error):
    
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404



@errors.app_errorhandler(403)    
def error_403(error):
        
    return jsonify({
        "success": False,
        "error": 403,
        "message": "Forbidden"
    }), 403




@errors.app_errorhandler(500)
def error_500(error):
        
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500



@errors.app_errorhandler(422)
def error_422(error):
        
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable Entity"
    }), 422
