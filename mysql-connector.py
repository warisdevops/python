import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='warriesa', passwd="0rangeB0x143", database="warries_db_storage")
mycursor = mydb.cursor()
mycursor.execute('select * from excel')
results= mycursor.fetchone()


for i in results:
    print(i)
