#!/bin/sh
############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' shell libraries           ##
############################################################################

## INCLUDES
. /usr/local/lib/depuydt/sh/echoes.sh

## TITLE
echo_section "DOCKER DEPLOYING:" "Automation Stack"

## Creating the volumes, networks and containers
docker-compose up --build --no-start

