from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta  #dbsparta라는 이름으로 접속

# 코딩 시작
#insert / find / update / delete

#----------- insert
# doc = {'name':'jane','age':21}
# db.users.insert_one(doc)

#----------- find - 여러개
# same_ages = list(db.users.find({'age':21},{'_id':False})) - 조건
same_ages = list(db.users.find({},{'_id':False}))

#----------- find - 하나만
user = db.users.find_one({'name':'bobby'},{'_id': False})
print(user)

#----------- update /// update_many : 조건에 해당하는 모든 걸 바꿔줘라 - 위험!.
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})


#----------- delete - 거의 안 씀  /// delete_many : 조건에 해당하는 모든 걸 바꿔줘라 - 위험!.
db.users.delete_one({'name':'bobby'})



