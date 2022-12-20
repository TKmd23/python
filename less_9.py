import sqlite3

connection = sqlite3.connect("test_10.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (tkmd TEXT);")
# cur.execute("INSERT INTO first_table (tkmd) VALUES ('Nick');")
# cur.execute("INSERT INTO first_table (tkmd) VALUES ('Kate');")
# cur.execute("INSERT INTO first_table (tkmd) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (tkmd) VALUES ('Jhon');")
cur.execute("SELECT rowid, tkmd FROM first_table;")
connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# cur.execute("UPDATE first_table SET name='TKmd' WHERE rowid=3;")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# connection.commit()
resp = cur.fetchall()
# # print(connection)
# print(cur)
print(resp[1][1])


# cur.execute("DELETE FROM first_table WHERE rowid=4;")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# resp = cur.fetchall()
# print(resp)

# cur.execute("DROP TABLE first_table;")
# connection.commit()

connection.close()