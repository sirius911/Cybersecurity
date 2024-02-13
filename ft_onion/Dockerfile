# Utiliser une image Debian
FROM debian:latest

ARG USER_NAME
ARG USER_PASS

# Installer Nginx, SSH et Tor
RUN apt-get update && apt-get install -y nginx openssh-server tor

# Ajouter un utilisateur avec les variables d'environnement passées
RUN useradd -m "$USER_NAME" && \
    echo "$USER_NAME:$USER_PASS" | chpasswd

RUN usermod -a -G debian-tor clorin

# Copier les fichiers de configuration et le site web
COPY ./config/nginx.conf /etc/nginx/nginx.conf
COPY ./config/sshd_config /etc/ssh/sshd_config
COPY ./config/torrc /etc/tor/torrc
COPY ./web /var/www/html
RUN chmod -R a+r /var/www/html

# Créer le répertoire du service caché pour debian-tor
RUN mkdir -p /var/lib/tor/hidden_service
RUN chown debian-tor:debian-tor /var/lib/tor/hidden_service
# Modifier les autorisations du répertoire web pour debian-tor
RUN chown -R debian-tor:debian-tor /var/www/html
RUN chmod 700 /var/lib/tor/hidden_service

# Ouvrir le port 80 pour Nginx et le port 4242 pour SSH
EXPOSE 80 4242

# Commandes pour démarrer les services
CMD service ssh start && service tor start && nginx -g 'daemon off;'
