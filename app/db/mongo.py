from pymongo import MongoClient

client = MongoClient(host='localmongo', port=27017, username='root', password='pass', authSource="admin")
db = client["user_db"]