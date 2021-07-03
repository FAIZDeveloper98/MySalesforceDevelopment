import sys
import pymysql

conn=pymysql.connect(host='jdbc:oracle:thin:@usadc-vzdb60:1521:TMODEV1',user='bus_met_datamart',password='bus_met_datamart',db='bus_met_datamart@TMODEV1')
if not conn:
    print("unable to connect to database")
    sys.exit(0)

try:
    cur=conn.cursor()
    cur.execute("create table books(bookid int,booktitle varchar(50))")
except pymysql.Error:
    print(sys.exc_info()[1])
    print("error in executing query")
else:
    print("table created")
finally:
    conn.close()
