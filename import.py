import pandas as pd
from influxdb import InfluxDBClient
import os

db = InfluxDBClient(host='localhost', port=8086)

df_full = pd.read_csv("data.csv")
df_full["measurement"] = ['FO' for t in range(len(df_full))]
lines = []
for d in range(len(df_full)):
    temp = \
    "jobname=%s" % str(df_full["jobname"][d]).replace(" ", "_") \
      + ",status=%s" % str(df_full["status"][d]).replace(" ", "_") \
      + " " \
      + "schedule_start_time=\"%s\"" % str(df_full["schedule_start_time"][d]) \
      + ",start_time=\"%s\"" % str(df_full["start_time"][d]) \
      + ",end_time=\"%s\"" % str(df_full["end_time"][d]) \
      + ",dutation_sec=\"%s\"" % str(df_full["duration_sec"][d]) \
      + ",dutation=\"%s\"" % str(df_full["duration"][d])
    lines.append(temp)
thefile = open('import.txt', '+a')
for item in lines:
    thefile.write("%s\n" % item)
trash = open("import.txt")
# db.write(lines, {'db':'test'},204,'line')
print(trash)
db.write_points(trash,database='test', protocol='line')

    # str(df_full.iloc[idx, -1]) \
    # + ",type=FreshOrders" + " " \
    # + "avg_FreshOrders=" \
    # + str(df_full.iloc[idx, 1]) \
    # + "," \
    # + "p95_FreshOrders=" \
    # + str(df_full.iloc[idx, 2]) \
    # + "," + "FreshOrders=" \
    # + str(df_full.iloc[idx, 3]) \
    # + " " \