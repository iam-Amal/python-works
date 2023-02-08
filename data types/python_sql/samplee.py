'''
# to insert table
import pymysql
db=pymysql.connect(host='localhost',user='root',password='Amal@3247',database='pythondb_test')
con=db.cursor()
sqlquery="insert into table2 values(%s,%s,%s)"
val=('manju',23,'idduki')
con.execute(sqlquery,val)
db.commit()
print('inserted')
'''

'''
#to insert values from keyboard
import pymysql
id=int(input('enter the id:'))
name=input('enter the name:')
age=int(input('enter the age:'))
place=input('enter the palce:')
db=pymysql.connect(host='localhost',user='root',password='Amal@3247',database='pythondb_test')
mycursor=db.cursor()
sql='insert into table2 values(%s,%s,%s,%s)'
val=(id,name,age,place)
mycursor.execute(sql,val)
db.commit()
print('inserted')
'''



#to delete table
'''
import pymysql
id=int(input('enter the id:'))
db=pymysql.connect(host='localhost',user='root',password='Amal@3247',database='pythondb_test')
mycursor=db.cursor()
sql="delete from table2 where id='%d'"%(id)
mycursor.execute(sql)
db.commit()
print('deleted')
'''

#to update a value
'''
import pymysql
y=input('do you want to update..? :')
if y== 'yes':
    db=pymysql.connect(host='localhost',user='root',password='Amal@3247',database='pythondb_test')
    id=int(input('enter the id :'))
    nm=input('enter the name:')
    ag=int(input('enter the age:'))
    c=db.cursor()
    sql="update table2 set name='%s',age='%d',where id='%d'"%(nm,ag,id)
    c.execute(sql)
    db.commit()
    print('updated')
else:
    print('exit')

'''
'''
import pymysql
id=int(input('enter the id:'))
db=pymysql.connect(host='localhost',user='root',password='Amal@3247',database='pythondb_test')
con=db.cursor()
sql='select * from table2 where id=%d'%id
con.execute(sql)
i=con.fetchone()
id = i[0]
na=i[1]
ag=i[2]

print(f'id={i[0]},name={na},age={ag}')
'''


import pymysql

db=pymysql.connect(host='localhost',user='root',password='Amal@3247',database='pythondb_test')
con=db.cursor()
sql='select * from table2'
con.execute(sql)
data=con.fetchall()
for i in data:
    id =i[0]
    na=i[1]
    ag=i[2]
    print(f'id={i[0]},name={na},age={ag}')