.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: build
build: ## Build the app
	docker build .

.PHONY: up
up:    ## Run the app
	docker-compose up --build fastapi-template

.PHONY: down
down: ## Stop and remove all the Docker services, volumes and networks
	docker-compose down -v --remove-orphans

.PHONY: dev
dev:    ## Run the server in dev mode
	uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

.PHONY: reformat
reformat:  ## Format python code
	ruff --fix src
	ruff format src
