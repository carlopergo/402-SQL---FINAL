import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='goat1234')
cursor = conn.cursor()
cursor.execute('DROP DATABASE IF EXISTS menagerie')
table = cursor.fetchall()
print(table)
conn.commit()
cursor.close()
conn.close()