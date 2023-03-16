import sqlite3

file_name = 'mySQLiteDB//myTestDB.db'
with sqlite3.connect(file_name) as conn:
    rs = conn.cursor()
    sqlData = "select no, name, high, weight, age from member"
    # rs.execute(sqlData)
    # rs1 = rs.fetchall()
    for row in rs.execute(sqlData):
        print(row)
    conn.commit()
