# Définition des variables par défaut
IMAGE_NAME := ft_onion
CONTAINER_NAME := ft_onion_container

# Commande pour construire l'image Docker
build:
	@read -p "Enter username: " username; \
	read -s -p "Enter password: " password; \
	echo "\n"; \
	docker build --build-arg USER_NAME=$$username --build-arg USER_PASS=$$password -t $(IMAGE_NAME) .

# Commande pour lancer le conteneur Docker
run:
	docker run -p 9050:9050 -p 80:80 -p 4242:4242 -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Cible pour récupérer l'adresse .onion
onion:
	@docker exec -it $(CONTAINER_NAME) cat /var/lib/tor/hidden_service/hostname

# Commande pour arrêter et supprimer le conteneur
clean:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)
	-ssh-keygen -f "/Users/$(USER)/.ssh/known_hosts" -R "[localhost]:4242"
