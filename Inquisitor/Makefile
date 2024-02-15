build: ## Start
	@ docker compose -f docker-compose.yaml up -d

inquisitor: ## Run the inquisitor
	@ docker exec -it inquisitor_container ./inquisitor $(shell utils/get_args)

status: ## Show the status of the containers
	@ docker ps

down: ## Stop
	@ docker compose -f docker-compose.yaml down

logs: ## Show the logs
	@ docker compose -f docker-compose.yaml logs

reload: ## Reload
	@ docker compose -f docker-compose.yaml up --build

client: ## Client demo
	@ docker exec -it client_container /usr/local/bin/script.exp

.PHONY: client inquisitor