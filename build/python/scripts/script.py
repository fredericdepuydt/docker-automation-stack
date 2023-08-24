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


sql = "SELECT * FROM 'HuaweiLUNA2000_ChargePower' WHERE time > '2023-04-25 04:00' AND time < '2023-04-25 11:30' "
results = list(client.query(sql).get_points())
filename = "HuaweiLUNA2000_ChargePower.csv"
f = open(filename, 'w')
f.write("time;value\n")
for result in results:
    time = str(result.get("time"))
    value = str(result.get("value"))
    f.write(time + ";" + value + "\n")
f.close()
    
exit()        
