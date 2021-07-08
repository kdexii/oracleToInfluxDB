import pandas as pd
from influxdb import InfluxDBClient
import os

db = InfluxDBClient(host='localhost', port=8086)

df_full = pd.read_csv("data.csv")
df_full["measurement"] = ['FO' for t in range(len(df_full))]
lines = []
for d in range(len(df_full)):
    temp = \
        "jobname=%s" % str(df_full.iloc[d,0])\
      + ",status=%s" % str(df_full.iloc[d,1])\
      + " " \
      + "schedule_start_time=\"%s\"" % str(df_full.iloc[d,2]) \
      + ",start_time=\"%s\"" % str(df_full.iloc[d,3]) \
      + ",end_time=\"%s\"" % str(df_full.iloc[d,4]) \
      + ",dutation_sec=\"%s\"" % str(df_full.iloc[d,5]) \
      + ",dutation=\"%s\"" % str(df_full.iloc[d,6])
      
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