import json
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
print(client)

my_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
#print(my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%'+'z'))
print(my_date)
x = {
     "t": str(my_date),
     "value": 42
     
 }
 
y=json.dumps(x)
print(y)
mydb = client["testdb"]
mytable = mydb["test"]
xx = mytable.insert_one(x)

print(xx.inserted_id)