# Project TODO List

RESTful principles are followed throughout the project, including appropriate naming of endpoints, use of HTTP methods GET, POST, and DELETE.
Routes perform CRUD operations on the psql database

## Backend TODO

### Utilize multiple HTTP request methods

	• [ x ] Endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.

	• [ x ] Endpoint to handle GET requests for all available categories.

	• [ x ] Endpoint to DELETE question using a question ID.

	• [ x ] Endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.

	• [ x ] Create a POST endpoint to get questions based on category.

	• [ x ] Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.

	• [ x ] Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.


### Handle common errors

	• [ x ] Project handles common errors using the @app.errorhandler decorator function to format an API friendly JSON error response
    • [ x ] Passes all provided tests related to error handling



