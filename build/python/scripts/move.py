#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
import sys

try:
    src = sys.argv[1]
    dst = sys.argv[2]
except Exception as e:
    raise e

from depuydt.database import influxdb
from pprint import pprint

client = influxdb.InfluxDBClient(host='influxdb.automation', port=8086)
client.switch_database('openhab')


#sql = "DROP SERIES FROM " + dst
#client.query(sql)

#sql = "SELECT * FROM " + str(src) + " WHERE \"value\" <> 1 AND \"value\" <> 0"
#pprint(client.query(sql))
#exit()

sql = "SELECT * FROM " + str(src)
results = list(client.query(sql).get_points())
print(str(len(results)) + " entries found for " + src)

data = []

for result in results:
    time = str(result.get("time"))
    value = result.get("value")
    data.append({
            "measurement": dst,
            "tags": {
                "user": "Python",
            },
            "time": time,
            "fields": {
                "value": value
            }
        })

client.write_points(data)


print(str(len(data)) + " entries written to " + dst)

sql = "DROP SERIES FROM " + src
client.query(sql)
        
