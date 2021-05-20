## Backend - Full Stack Trivia API 


3. **PIPENV Dependencies** 
Ensure your pipenv environment is installed and running as shown [here](../readme.md)

Install all requiremnents using:
```bash
pipenv install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./backend` directory, with your pipenv environment running, start the server with 


```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.



## Testing
To create the test database, on a terminal run 

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
```
Once the database is running, run the test file

```
python test_trivia.py
```

Ensure all tests run successfully.