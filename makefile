run:
	@uvicorn src.main:app --reload

precommit-install:
	@poetry run pre-commit install
