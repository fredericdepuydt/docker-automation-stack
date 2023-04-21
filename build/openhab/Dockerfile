FROM openhab/openhab:3.4.1
LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
RUN apt-get update && \
    apt-get install -y dnsmasq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
