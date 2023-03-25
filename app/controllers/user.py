from flask import jsonify, request
from db.mongo import db
from utils.jwt import encode_token

def list_users():
    _users = db.user_tb.find()
    
    users = []
    for user in _users:
        users.append({"username": user["username"], "password": user["password"]})
            
    return jsonify({"users": users}) 


def create_user():
    data = request.form
    nome = data['username']
    senha = data['password']
    
    db.user_tb.insert_one({'username': nome, 'password': senha})
    
    return jsonify({'mensagem': 'Usuário criado com sucesso!'})


def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    user = db.user_tb.find_one({"username": username, "password": password})
    if user:
        payload = {"username": username}
        token = encode_token(payload)
        return {'mensagem': f'Token para o usuário: {username} criado com sucesso!',"token": token}
    else:
        return {'mensagem': 'Campos de usuário ou senha inválidos'}