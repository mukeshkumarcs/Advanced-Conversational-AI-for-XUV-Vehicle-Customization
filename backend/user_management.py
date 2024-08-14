from pymongo import MongoClient
import bcrypt

client = MongoClient('mongodb://localhost:27017/')
db = client['xuv_chatbot']
users = db['users']

def create_user(username, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = {
        "username": username,
        "password": hashed,
        "preferences": {}
    }
    users.insert_one(user)

def update_user_preference(username, feature, value):
    users.update_one(
        {"username": username},
        {"$set": {f"preferences.{feature}": value}}
    )
