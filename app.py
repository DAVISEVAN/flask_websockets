from flask import Flask, jsonify
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@socketio.on('message')
def handle_message(data):
    username = data.get('username')
    message = data.get('message')
    user = User(username=username, message=message)
    db.session.add(user)
    db.session.commit()
    send(f"{username}: {message}", broadcast=True)

@app.route('/all_users', methods=['GET'])
def all_users():
    users = User.query.all()
    return jsonify({
        "users": [{"username": user.username, "message": user.message} for user in users]
    })

if __name__ == '__main__':
    socketio.run(app, debug=True)
