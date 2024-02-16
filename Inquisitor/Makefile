
inquisitor: ## Run the inquisitor
	-@ docker exec -it inquisitor_container ./inquisitor $(shell utils/get_args)

status: ## Show the status of the containers
	@ docker ps

down: ## Stop
	@ docker compose -f docker-compose.yaml down

logs: ## Show the logs
	@ docker exec -it ftp_container cat /var/log/vsftpd.log

up: ## up
	@ docker compose -f docker-compose.yaml up

simule_client: ## simulation client
	@ docker exec -it client_container /usr/local/bin/script.exp

client: ## lien shell
	@ docker exec -it client_container sh

ftp: ## lien shell
	@ docker exec -it ftp_container sh 

info:
	python utils/get_args --info

stop_inquisitor:
	@docker exec inquisitor_container pkill -f 'python3 ./inquisitor'

build:
	docker-compose build --no-cache

fclean:  down ## Clean and prune the docker system
	@ docker system prune -af

.PHONY: client inquisitor build simule_client logs stop_inquisitor 