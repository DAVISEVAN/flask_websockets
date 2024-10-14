# from flask import Flask, jsonify
# from flask_socketio import SocketIO, send
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interactions.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# socketio = SocketIO(app, cors_allowed_origins="*")

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     message = db.Column(db.String(200), nullable=False)

# with app.app_context():
#     db.create_all()

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')

# @socketio.on('message')
# def handle_message(data):
#     username = data.get('username')
#     message = data.get('message')
#     user = User(username=username, message=message)
#     db.session.add(user)
#     db.session.commit()
#     send(f"{username}: {message}", broadcast=True)
    
# @app.route('/all_users', methods=['GET'])
# def all_users():
#     users = User.query.all()
#     return jsonify({
#         "users": [{"username": user.username, "message": user.message} for user in users]
#     })

# if __name__ == '__main__':
#     socketio.run(app, debug=True)
from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# Initialize Flask app and Flask-SocketIO
app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask app
socketio = SocketIO(app, cors_allowed_origins='http://localhost:5173')  # Vite dev server

# Handle WebSocket connections
@socketio.on('connect')
def handle_connect():
    print('A client connected')

# Handle incoming 'message' events
@socketio.on('message_client')
def handle_message(msg):
    print('Received message:', msg)
    emit('message', msg, broadcast=True)  # Broadcast message to all clients

# Handle client disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print('A client disconnected')

# Start the server
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)


