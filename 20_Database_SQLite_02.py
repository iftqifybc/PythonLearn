import sqlite3
conn = sqlite3.connect('mySQLiteDB/example.db')
# sql = "select * from member, orders where member.id == orders.member_id and member.id='V123456786'"
# sql = "select * from member, orders where member.id == orders.member_id"
# sql = "select * from orders inner join member on orders.member_id = member.id where member.id='V123456786'"
sql = "select * from member inner join orders on member.id = orders.member_id where member.id='V123456786'"
# sql = 'select * from member'
# sql = "select * from orders, orders_detail where o"
rs = conn.execute(sql)
# rs = conn.cursor()
#sql = "CREATE TABLE member (id	INTEGER, 	name	TEXT,  phone 	TEXT, addr	TEXT);"
#rs.execute(sql)
# sql = "insert into member values(1,'小黑','0910000001','新北市永和區')"
#rs.execute(sql)
#sql = "insert into member values(2,'小黃','0910000002','新北市中和和區')"
#rs.execute(sql)
#sql = "insert into member values(3,'小花','0910000003','新北市新莊區')"
#rs.execute(sql)
#sql = "insert into member values(4,'小白','0910000004','新北市三重區')"
#rs.execute(sql)

# for row in rs.execute(sql):
for row in rs.fetchall():
    print(row)
    # if row[1] == '小花':
    #     print(f'say hi:{row[1]}')
conn.commit()
conn.close()