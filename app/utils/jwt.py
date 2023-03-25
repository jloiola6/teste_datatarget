import jwt

secret_key = 'jaiHQ99123kanIUmso1plsad>As1/hdiu'

def encode_token(payload):
    return jwt.encode(payload, secret_key, algorithm="HS256")