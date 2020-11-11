# Example Flask app

### Setting up
1. Create a Python3 virtual environment and activate it.
2. Install dependencies by running: `pip install -r requirements.txt`
3. Initialize db by running: `python library_app/models.py`

### Running the app
```python run.py```

### Guide to the code:
1. The API requests are defined in views.py
2. All the database models are defined in models.py
3. Logging configuration is defined in `library_app/__init__.py`

### Testing
* Running the tests: `pytest`
* For coverage, run: 
1. `coverage -m pytest`
2. `coverage html`
3. Open `/htmlcov/index.html` in the browser