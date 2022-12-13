import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.r0xf715.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# target_movie = db.movies.find_one({'title':'가버나움'})
# print(target_movie['star'])

# target_movie = db.movies.find_one({'title':'가버나움'})
# target_star = target_movie['star']
#
# movies = list(db.movies.find({'star':target_star}))
#
# for movie in movies:
#     print(movie['title'])

db.movies.update_one({'title':'가버나움'}, {'$set': {'star':'0'}})
