import mysql.connector
#CONNECTIVITY

myconn=mysql.connector.connect(host="localhost",user="root",database="world",passwd="root")
if(myconn.is_connected()):
    str="SELECT * FROM city LIMIT 10"
    curs=myconn.cursor()
    curs.execute(str)
    data=curs.fetchall()
    #print(type(data))
    #print(data,end="\n")
    for record in data:
             print(record,'\n')
           
   
else:
    print('Connection Failed')
    