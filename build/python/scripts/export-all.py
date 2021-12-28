#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################

## INCLUDES
from depuydt.database import influxdb
from pprint import pprint



client = influxdb.InfluxDBClient(host='influxdb.automation', port=8086)
client.switch_database('openhab')

tables = list(client.query("show measurements").get_points())
for table in tables:
    name = table.get("name")
    sql = "SELECT * FROM " + str(name)
    results = list(client.query(sql).get_points())
    filename = name + ".csv"
    f = open(filename, 'w')
    f.write("time;value\n")
    for result in results:
        time = str(result.get("time"))
        value = str(result.get("value"))
        f.write(time + ";" + value + "\n")
    f.close()
