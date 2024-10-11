# Instructions for setting up the Flask WebSocket backend

# 1. Clone the repository:

git clone <repository_url>
cd flask_websockets

# 2. Install Python
# On MacOs 

# 3. Set up a Python virtual environment and activate it:
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies:
pip install flask flask-socketio flask-sqlalchemy

# 5. Run the Flask app:
python app.py

# 6. REST API Endpoint:
# After running the app, you can access the list of all users by going to:
# http://localhost:5000/all_users

# Example JSON Response:
# {
#   "users": [
#     {
#       "username": "Alice",
#       "message": "Hello, this is Alice!"
#     },
#     {
#       "username": "Bob",
#       "message": "Hey, Bob here!"
#     }
#   ]
# }

# 7. WebSocket Functionality:
# WebSocket messages can be sent and received via the Flask-SocketIO connection.
# The WebSocket URL is ws://localhost:5000
# Example message format:
# {
#   "username": "Anonymous",
#   "message": "Hello, World!"
# }

# 8. Frontend React Setup:
# In the React app, fetch the users and set up WebSocket communication something like this example from :

import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

function App() {
  const [message, setMessage] = useState('');
  const [currentString, setCurrentString] = useState('');
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Fetch users from the Flask API
    fetch('http://localhost:5000/all_users')
      .then(response => response.json())
      .then(data => {
        setUsers(data.users);
      });

    // Set up WebSocket to receive messages
    socket.on('message', (data) => {
      setCurrentString(data);
    });

    return () => {
      socket.off('message');
    };
  }, []);

  const sendMessage = (e) => {
    e.preventDefault();
    socket.send({ username: "Anonymous", message: message });
    setMessage('');
  };

  return (
    <div>
      <h1>Live Text Input</h1>
      <p>Current text: {currentString}</p>
      <form onSubmit={sendMessage}>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>

      <h2>Users:</h2>
      <ul>
        {users.map((user, index) => (
          <li key={index}>
            {user.username}: {user.message}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

# Now the Flask backend can interact with the React frontend, allowing real-time messaging and user data display.

