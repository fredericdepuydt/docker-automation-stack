FROM openhab/openhab:4.1.2
LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL release-date="2024-04-01"
RUN apt-get update && \
    apt-get install -y dnsmasq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
