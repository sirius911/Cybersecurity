all: help

help:
	@ grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build all the 3 containers ftp_server, client and inquisitor
	docker-compose build --no-cache

up: ## start the containers
	@ docker compose -f docker-compose.yaml up

down: ## Stop the containers
	@ docker compose -f docker-compose.yaml down

re: down build up## Rebuild and relauch Containers


inquisitor: ## Run the inquisitor
	-@ docker exec -it inquisitor_container ./inquisitor $(shell utils/get_args)

inquisitor-verbose: ## Run the inquisitor
	-@ docker exec -it inquisitor_container ./inquisitor --verbose $(shell utils/get_args)

status: ## Show the status of the containers
	@ docker ps

logs: ## Show the logs of ftp_server (vsftpd.log)
	@ docker exec -it ftp_container cat /var/log/vsftpd.log

simule_client: ## run the simulation of a client ftp (script.exp)
	@ docker exec -it client_container /usr/local/bin/script.exp

client: ## shell in client container
	@ docker exec -it client_container sh

ftp: ## shell in ftp_container
	@ docker exec -it ftp_container sh

shell_inquisitore: ## shell in inquisitor_container
	@ docker exec -it inquisitor_container sh

info: ## information IP/MAC/ARP 
	utils/get_args --info

args: ## give arguments of containers info for inquisitor
	utils/get_args

fclean:  down ## Clean and prune the docker system
	@ docker system prune -af

.PHONY: client inquisitor build simule_client logs re help