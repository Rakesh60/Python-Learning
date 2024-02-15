import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
print(myconn)