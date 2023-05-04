import sqlite3


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('testdb.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
# cursor.execute('''
# INSERT INTO users (
#     name,
#     email
# )
# VALUES ("Marina", "truten@gmail.com")
# ''')

# cursor.executescript('''
# INSERT INTO users (name, email) VALUES ("Joe", "Joe@gmail.com");
# INSERT INTO users (name, email) VALUES ("Kate", "Kate@gmail.com");
# ''')
# -----------------
# users_data = [
#     ('User 1', 'user1@gmail.com'),
#     ('User 2', 'user2@gmail.com'),
#     ('User 3', 'user3@gmail.com'),
#     ('User 4', 'user4@gmail.com'),
#          ]
# cursor.executemany('''
# INSERT INTO users (name, email) VALUES (?, ?)
# ''', users_data)
# ---------------

# email = 'kkotolup@gmail.com'
# name = "Joe"
# # cursor.execute('''
# # SELECT * FROM users WHERE email = ? OR name = ?
# # ''', (email, "Joe"))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email, 'name': name})
# resultat = cursor.fetchone()
# ------------------
cursor.execute("SELECT * FROM users")
resultat = cursor.fetchall()
print(resultat)

for i in resultat:
    print(i['name'], i['email'])
# db.commit()

db.close()
