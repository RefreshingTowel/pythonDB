import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute("INSERT INTO USERS (USERID,NAME,CELL,CHATID,GROUPID,BROKER) \
      VALUES ('Giacomodelbono', 'Giacomo Del Bono', 3336927478, '846839325', 'groupid','Binance' )");

conn.execute("INSERT INTO GROUPS (GROUPID,NAME,TYPE,TARIFFA,USERID) \
      VALUES (1001288385100,'Whales Crypto Guide','','','Giacomodelbono')");

conn.execute("INSERT INTO BROKERS (NAME,TYPE,TARIFFA) \
      VALUES ('Binance','','')");

conn.execute("INSERT INTO APIKEYS (API,USERID,BROKERNAME) \
      VALUES ('y1i5knoswzqcUVMf86asRYsThfEKlZyBQijEtG3d2y4f98Q8dWStnrRtYiRdq3I','Giacomodelbono','Binance')");

conn.commit()
print("Records created successfully");
conn.close()