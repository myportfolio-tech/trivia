# Project TODO List

### Write clear, concise and well documented code

	• [ x ] Variable and function names are clear.

	• [ x ] Endpoints are logically named.

	• [ x ] Code is commented appropriately.

	• [ x ] The README file includes detailed instructions for scripts to install any project dependencies, and to run the development server.

### Write an informative README File

	• [ x ] Instructions for how to install project dependencies and start the project server.

	• [ x ] Detailed documentation of API endpoints and expected behavior, using the format taught in the course:
		○ METHOD Url
			Request parameters
			Response body
 
### RESTful principles are followed throughout the project

	• [ x ] appropriate naming of endpoint.

	• [ x ] use of HTTP methods GET, POST, and DELETE.

	• [ x ] Routes perform CRUD operations on the psql database

## Backend TODO

### Utilize multiple HTTP request methods

	• [ x ] Endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.

	• [ x ] Endpoint to handle GET requests for all available categories.

	• [ x ] Endpoint to DELETE question using a question ID.

	• [ x ] Endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.

	• [ x ] Create a POST endpoint to get questions based on category.

	• [ x ] Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.

	• [ x ] Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question 				parameters and return a random questions within the given category, if provided, and that is not one of the previous 			questions.


### Handle common errors

	• [ x ] Project handles common errors using the @app.errorhandler decorator function to format an API friendly JSON error response
    • [ x ] Passes all provided tests related to error handling


### Unittest Flask Application

	• [ x ] Import and utilize unittest library to test each endpoint for expected success and error behavior. Each endpoint should 		have at one test for the expected behavior and tests for error handling if applicable.
    • [ x ] Project includes tests to ensure CRUD operations are successfu



