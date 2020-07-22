#### URLS
# https://github.com/EugenMayer/docker-image-zway
# https://github.com/sofakng/docker-zway
# https://github.com/ruimarinho/docker-z-way/

FROM multiarch/debian-debootstrap:armhf-buster-slim

LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL release-date="2020-07-22"

ENV ARCH armhf

RUN apt-get update
RUN apt-get install -y supervisor ca-certificates

RUN wget -q -O /tmp/z-way-3.0.6_armhf.deb https://storage.z-wave.me/z-way-server/z-way-3.0.6_armhf.deb
RUN apt install -y /tmp/z-way-3.0.6_armhf.deb 

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup supervisord to monitor/autorestart
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Export the web interface port
EXPOSE 8083

# Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]