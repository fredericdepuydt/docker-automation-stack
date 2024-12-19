#### URLS
# https://github.com/EugenMayer/docker-image-zway
# https://github.com/sofakng/docker-zway
# https://github.com/ruimarinho/docker-z-way/

#### NOTE !!!
# To make /dev/ttyAMA0 available on Raspberry Pi
# - Disable bluetooth in /boot/config.txt -> dtoverlay=disable-bt (Add this part)
# - Disable serial console in /boot/cmdline.txt -> console=serial0,115200 (Remove this part)
# - Stop services:
#     sudo systemctl disable hciuart.service
#     sudo systemctl disable bluealsa.service
#     sudo systemctl disable bluetooth.service
# - Uninstall bluetooth
#     sudo apt-get purge bluez -y
#     sudo apt-get autoremove -y
#

#### NOTE 2
# Requires 'buster' for packages like:
#  - libssl1.1
#  - libwebsockets8
#  - libwebsockets16
FROM debian:buster-slim


LABEL maintainer="Frederic Depuydt <frederic.depuydt@outlook.com>"
LABEL release-date="2024-08-20"

ENV ARCH armhf

RUN apt-get update
RUN apt-get install -y supervisor ca-certificates wget

RUN wget -q -O /tmp/z-way.deb https://storage.z-wave.me/z-way-server/z-way-4.1.4_armhf.deb
RUN apt install -y /tmp/z-way.deb

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup supervisord to monitor/autorestart
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Export the web interface port
EXPOSE 8083

# Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]