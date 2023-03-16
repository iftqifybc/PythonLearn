#https://sqlitebrowser.org/blog/apple-silicon-macos-package-available/

# CREATE DATABASE testDB;
# DROP DATABASE testDB;
# CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );
# DROP TABLE Shippers;
# connection database
# # -*- coding: utf-8 -*-
# import sqlite3
# db = sqlite3.connect('TEST.db')
# cursor = db.cursor()
# print('Connect ok')
# # Create table
# cursor.execute(
# '''CREATE TABLE HUMAN
# (ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# AGE INT NOT NULL);''')
#
# print('Table created.')
# db.commit()
import sqlite3
file_name = 'mySQLiteDB//myTestDB.db'
conn = sqlite3.connect(file_name)
rs = conn.cursor()

# # Insert
# cursor.execute('''INSERT INTO HUMAN (ID,NAME,AGE) VALUES (1, 'Clay', 25)''')
# cursor.execute('''INSERT INTO HUMAN (ID,NAME,AGE) VALUES (2, 'Wendy', 16)''')
#
# db.commit()
# print('Insert ok')

# # Select
# results = cursor.execute('''SELECT * FROM HUMAN''')
# for item in results:
#     print(item)

# # Update
def updateData():
    member = input('enter update member:')
    id = input('enter update id:')
    results = rs.execute("UPDATE HUMAN set AGE = 26 WHERE ID = '1'")
    # db.commit()

# # Delete
def deleteData():
    member = input('enter delete member:')
    rs.execute('''DELETE FROM member WHERE ID = 2''')
    conn.commit()
# db.close() #close database

def insertData():
    # sqlData = "insert into member values(4, 'sky',166,50,35)"
    sqlData = "insert into member values("
    num = input("enter no:")
    name = input("enter name:")
    high = input("enter high:")
    weight = input("enter weight:")
    age = input("enter age:")
    sqlData += num + ", "
    sqlData += "'" + name + "',"
    sqlData += high + ", "
    sqlData += weight + ", "
    sqlData += age + ")"
    # print(sqlData)
    rs.execute(sqlData)
    conn.commit()


def selectData():
    sqlData = "select no, name, high, weight, age from member where no > 5"
    rs.execute(sqlData)
    print(f"rowcount:{rs.execute(sqlData).rowcount}")
    rs1 = rs.fetchall()
    if rs1:
        for row in rs1:
            # print(f"row:{row}")
            # print(f"data 0:{row[0]}")
            print(f"num:{row[0]}, name:{row[1]}  high:{row[2]}  weight:{row[3]}  age:{row[4]}")
            # print(row)
    else:
        print("no data")


def main():
    while True:
        ch = input("enter (1)insert (2)select (3)update (4)delete (0)quit\n")
        if ch == "1":
            insertData()
        elif ch == "2":
            selectData()
        elif ch == '3':
            updateData()
        elif ch == '4':
            deleteData()
        else:
            break

if __name__ == '__main__':
    main()
conn.close()