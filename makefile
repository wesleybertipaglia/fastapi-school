run:
	@uvicorn src.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb store ./tests/

docker-up:
	@docker-compose up -d

docker-down:
	@docker-compose down
