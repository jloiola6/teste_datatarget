from flask import Flask
from doc.swagger import swagger_blueprint
from controllers.user import list_users, create_user, login
from controllers.cep import cep_details
from logs.elasticsearch import log_request, all_logs

app = Flask(__name__)
app.register_blueprint(swagger_blueprint)
app.before_request(log_request)

@app.route('/user/list')
def get_users():
    return list_users()

@app.route('/user/create', methods=['POST'])
def post_users():
    return create_user()

@app.route('/user/login', methods=['POST'])
def create_token():
    return login()

@app.route("/api/cep", methods=["POST"])
def weather():
    return cep_details()

@app.route('/api/logs', methods=['GET'])
def get_logs(): 
    return all_logs()
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    