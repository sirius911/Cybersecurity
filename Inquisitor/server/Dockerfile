# Utiliser Alpine Linux comme image de base
FROM alpine:3.12

# Installation de vsftpd et iproute2 (pour arp)
RUN apk add --update vsftpd iproute2 net-tools && \
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

# Ajuster les permissions et la propriété de /ftp et ses sous-répertoires
# Changer la propriété de /ftp à l'utilisateur ftp
RUN chown ftp:ftp /ftp -R
# Définir les permissions appropriées pour /ftp et /ftp/data
RUN chmod 755 /ftp && chmod 775 /ftp/data


# config client
RUN chmod a-w /home/client

RUN mkdir /home/client/upload
RUN chmod a+w /home/client/upload

# Copier les fichiers dans le dossier /ftp/data
COPY data/ /ftp/data

# Créer le fichier de journalisation vsftpd.log avec les bonnes permissions
RUN touch /var/log/vsftpd.log && chown ftp:ftp /var/log/vsftpd.log

# Exposer le port FTP standard
EXPOSE 21

# Commande pour démarrer vsftpd
CMD ["vsftpd", "/etc/vsftpd/vsftpd.conf"]

