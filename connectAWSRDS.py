import MySQLdb as ms

myDB = ms.connect(host = "raj.cjvevq7bmlpd.eu-central-1.rds.amazonaws.com", user = "raj", passwd = "Rajashekar123", db = "rajDB")
cur = myDB.cursor()
cur.execute("select * from sampel")
query = cur.fetchall()
print query

cur.close()
myDB.close()