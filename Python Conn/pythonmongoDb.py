#INSTALL PYMONGO
#command: pip install pymongo
# mongodb://localhost:27017

import pymongo

#CONNECTIVITY
client=pymongo.MongoClient('mongodb://localhost:27017')

#CREATE A DB 

mydb=client['pythondb']
# #CREATE A COLLECTION
mycollection=mydb['Python_collection']
#CREATE A DOCUMENT
# mydoc={'name':'Rakesh','address':'Bengaluaru'}

# # #INSERT DOCUMENT
# res=mycollection.insert_one(mydoc)
# dbs=client.list_database_names()
# # print(dbs[0:len(dbs)])
# print(dbs.index('pythondb'))

#READING
# r=mycollection.find_one()
# print(r)


#UPDATING
# update={'address':'Bengaluaru'}

# new_var={'$set':{'address':'I live in Patna'}}

# new_doc=mycollection.update_one(update,new_var)
# print(new_doc)

#Reading the doc after updating
# r=mycollection.find()
# print(r)

#DELETE THE RECORD
# query_del={'name':'Rakesh'}
# doc_del=mycollection.delete_one(query_del)

# r=mycollection.find_one()
# print(r)




