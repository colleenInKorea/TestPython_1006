from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.r0xf715.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# 모든 데이터 뽑아보기
# all_users = list(db.users.find({},{'_id':False}))
#
# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기
#
# for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
#     print(user)

# db.users.update_one({'name':'bobby'}, {'$set':{'age':19}})
#
# user = db.users.find_one({'name':'bobby'})
# print(user)

db.users.delete_one({'name':'bob'})

user = db.users.find_one({'name':'bob'})
print(user)