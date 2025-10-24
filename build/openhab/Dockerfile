FROM openhab/openhab:5.1.0.M1
LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL release-date="2025-10-24"
RUN apt-get update && \
    apt-get install -y dnsmasq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
