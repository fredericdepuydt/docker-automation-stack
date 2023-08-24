#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
import sys
import csv
from pprint import pprint
from datetime import datetime

from depuydt.database import influxdb
from pprint import pprint

client = influxdb.InfluxDBClient(host='influxdb.automation', port=8086)
client.switch_database('openhab')
i = 1
while( i <= len(sys.argv)):
    try:
        src = sys.argv[i]
    except Exception as e:
        raise e
    print("Deleting from " + src)
    sql = "DROP MEASUREMENT " + src
    client.query(sql)
    i = i + 1
    

exit()        
