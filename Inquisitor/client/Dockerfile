FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y ftp expect net-tools

COPY script.exp /usr/local/bin/

COPY ./rep/ ./

RUN chmod +x /usr/local/bin/script.exp

# ENTRYPOINT ["/usr/local/bin/script.exp"]

#en attente
CMD ["tail", "-f", "/dev/null"]