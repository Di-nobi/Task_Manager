from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from api.v1.views import app_look
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.register_blueprint(app_look)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "secret_key")

cors = CORS(app, resources={r"/*": {"origins": "*"}})
jwt = JWTManager(app)

app.config['SWAGGER'] = {
    'title': 'Task Management App',
    'uiversion': 3
}

Swagger(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.errorhandler(404)
def notFound(err):
    return jsonify({'error': f'Not found {err}'}), 404

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='5000', debug=True)