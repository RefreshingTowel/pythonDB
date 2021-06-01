import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully");

conn.execute('drop table if exists USERS')

conn.execute('''CREATE TABLE USERS
         (USERID        INT     PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         CELL           INT     NOT NULL,
         CHATID         INT     NOT NULL,
         GROUPID        TEXT,
         BROKER         TEXT    NOT NULL,
         FOREIGN KEY (GROUPID) REFERENCES GROUPS (GROUPID)
         );''')
print("Table USERS created successfully");

conn.execute('drop table if exists GROUPS')

conn.execute('''CREATE TABLE GROUPS
         (GROUPID INT PRIMARY KEY     NOT NULL,
         NAME            TEXT    NOT NULL,
         TYPE            TEXT    NOT NULL,
         TARIFFA         INT,
         USERID          TEXT    NOT NULL,
         FOREIGN KEY (USERID) REFERENCES USERS (USERID)
         );''')
print("Table GROUPS created successfully");

conn.execute('drop table if exists BROKERS')

conn.execute('''CREATE TABLE BROKERS
         (NAME TEXT PRIMARY KEY     NOT NULL,
         TYPE            TEXT    NOT NULL,
         TARIFFA         INT
         );''')
print("Table BROKERS created successfully");

conn.execute('drop table if exists APIKEYS')

conn.execute('''CREATE TABLE APIKEYS
         (API TEXT PRIMARY KEY     NOT NULL,
         USERID            TEXT    NOT NULL,
         BROKERNAME        TEXT    NOT NULL,
         FOREIGN KEY(USERID) REFERENCES USERS(USERID),
         FOREIGN KEY (BROKERNAME) REFERENCES BROKERS (NAME)
         );''')
print("Table APIKEYS created successfully");


conn.close()
