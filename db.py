import sqlite3 as sql

# connect to db
connection = sql.connect('test.sqlite')

# create cursor to work with cursor
q = connection.cursor()

# q.execute(''' CREATE TABLE user (id int auto_increment primary key, name varchar,  password varchar )''')
# connection.commit()

user_name = input("Enter your name:  ")
user_password = input("Enter your password: ")

print("User list:]\n")
q.execute("INSERT INTO user (name, password) VALUES ('%s', '%s')"%(user_name, user_password))
connection.commit()

q.execute("SELECT * FROM user ")
row =  q.fetchone()

while row is not None:
    print("Name:", row[1], "| Password:", row[2])
    row = q.fetchone()

# disconnect from db
q.close()