#!/usr/bin/env python3

############################################################################
## Raspberry-Pi installation script                                       ##
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
##                                                                        ##
## Executing this script requires the 'depuydt' python libraries          ##
############################################################################

## INCLUDES
import sys
sys.path.insert(1, '/usr/local/lib/depuydt/python/')

import os

from echo import echo
from docker import docker
from command import command

## TITLE
echo.section("DOCKER EXPORTING", "Docker Automation Stack (Exporting)");

## Exporting

os.mkdir("export");
os.mkdir("export/openhab");
docker.cp("openhab:/openhab/conf","export/openhab/conf");
docker.cp("openhab:/openhab/userdata","export/openhab/userdata");


