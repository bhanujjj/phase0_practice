run:
	uvicorn src.main:app --reload

test:
	pytest

build:
	docker compose up --build

down:
	docker compose down
