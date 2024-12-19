FROM openhab/openhab:4.3.0
LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL release-date="2024-12-19"
RUN apt-get update && \
    apt-get install -y dnsmasq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
