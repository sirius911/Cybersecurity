# Utiliser Alpine Linux comme image de base
FROM alpine:3.12

# Installation de vsftpd et iproute2 (pour arp)
RUN apk add --update vsftpd iproute2 && \
    rm -rf /var/cache/apk/*

# Ajouter un utilisateur pour le client FTP
RUN adduser -D client && echo "client:password" | chpasswd

# Configuration de vsftpd
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf
RUN echo "client" > /etc/vsftpd/user_list
RUN chmod 644 /etc/vsftpd/user_list


RUN mkdir -p /var/run/vsftpd/root

# Créer un dossier pour les fichiers FTP
RUN mkdir -p /ftp/data

# Copier les fichiers dans le dossier /ftp/data
COPY data/ /ftp/data

# Exposer le port FTP standard
EXPOSE 21

# Commande pour démarrer vsftpd
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]

