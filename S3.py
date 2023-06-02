import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='goat1234')
cursor = conn.cursor()
cursor.close()
conn.close()