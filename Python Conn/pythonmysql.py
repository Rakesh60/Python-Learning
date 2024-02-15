import mysql.connector #always write import statement for connection

#CONNECTIVITY

myconn=mysql.connector.connect(host="localhost",user="root",passwd="")
if(myconn.is_connected()):
    print('Connection Successfull')
else:
    print(ConnectionError)
    
curs=myconn.cursor()
# curs.execute("CREATE DATABASE pythonDB")

#creating Table

# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# str="CREATE TABLE book(u_id int(4),title varchar(20),Amount float(5,2))"
# curs=myconn.cursor()
# curs.execute(str)

#Inserting Values
# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# str="Insert into book(u_id,title,Amount) Values(%s,%s,%s)"
# b1=(101,'Wings of fire',899)
# curs=myconn.cursor()
# curs.execute(str,b1)
# myconn.commit()

#INSERT MULTIPLE VALUES
# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# str="Insert into book(u_id,title,Amount) Values(%s,%s,%s)"
# books=[(102,'Half-Girlfriend',499),(103,'Ignited Minds',799),(104,'INDIA-2047',1099)]
# curs=myconn.cursor()
# curs.executemany(str,books)
# myconn.commit()

#Extracting Data
# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# str="SELECT * FROM book"
# curs=myconn.cursor()
# curs.execute(str)
# data=curs.fetchall()

# for booksdata in data:
#     print(booksdata)


# #updating DAta
# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# str="update book set Amount=2999 where Amount=1099"
# curs=myconn.cursor()
# curs.execute(str)
# myconn.commit()

#updating DAta
# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# str="Delete from book where Amount=2999"
# curs=myconn.cursor()
# curs.execute(str)
# myconn.commit()


# myconn=mysql.connector.connect(host="localhost",user="root",passwd="",database="pythondb")
# # str="INSERT INTO profile(u_id,title,Amount) Values(2,'kumar',499)"
# # curs=myconn.cursor()
# # curs.execute(str)
# # myconn.commit()
# print(myconn)
# print(id(myconn))


