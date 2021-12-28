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

try:
    src = sys.argv[1]
except Exception as e:
    raise e


with open("manipulated/" + src + ".csv") as csv_file:          
    data = []
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            dt = datetime.utcfromtimestamp(int(row[0])//1000000000)
            t = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            try:
                data.append({
                    "measurement": src,
                    "tags": {
                        "user": "Python",
                    },
                    "time": t,
                    "fields": {
                        "value": int(row[1])
                    }
                })
            except Exception:
                pass
    ##pprint(data)            
    client.write_points(data)
exit()        
