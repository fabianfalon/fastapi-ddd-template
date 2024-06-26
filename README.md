## Fastapi DDD hexagonal architecture

🐍 Basic example of a Python & Fastapi application using Domain-Driven Design.

## Local run
````pip install -r requirements.txt```` or ````pip install -r requirements-tests.txt````
___
````uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload````

### Run test
````python -m pytest````

````python -m pytest --cov=src````

# Ruff commands
Check linters errors
````ruff check src````

Check format errors
````ruff format -- check src````

Fix imports order

````ruff --fix src````

Fix file format

````ruff format src````
