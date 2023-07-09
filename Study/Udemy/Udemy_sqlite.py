import sqlite3

DB_NAME = 'sqlite_db.db'

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = '''CREATE TABLE IF NOT EXISTS courses (
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );'''
#     sqlite_conn.execute(sql_request)


#Adding to DB
# courses = [
#     (351, 'Java', 12, 48),
#     (222, 'Test', 3, 8),
#     (112, 'Check', 4, 22),
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = 'INSERT INTO courses VALUES(?, ?, ?, ?)'
#     # sqlite_conn.execute(sql_request, (2307, 'tkmd', 1, 36))
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = 'SELECT * FROM courses WHERE reviews_qty>=30'
    cursor = sqlite_conn.execute(sql_request)
    # for i in cursor:
    #     print(i)
    records = cursor.fetchall()
    print(records)