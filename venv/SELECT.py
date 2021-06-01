import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

cursor = conn.execute("SELECT USERID,NAME,CELL,CHATID from USERS")
for row in cursor:
   print("USERID = ", row[0])
   print("NAME = ", row[1])
   print("CELL = ", row[2])
   print("CHATID = ", row[3], "\n")





print("Operation done successfully");
conn.close()