import React, { useState } from 'react';
import { UserContext } from '../contexts/UserContext';
import { ChatContext } from '../contexts/ChatContext';
import Login from '../components/Login/Login';
import ChatApp from '../components/ChatApp/ChatApp';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [chatMessages, setChatMessages] = useState([]);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      <ChatContext.Provider value={{ chatMessages, setChatMessages }}>
      <div className="App">
          {!user ? <Login onLogin={setUser} /> : <ChatApp user={user} />}
        </div>
      </ChatContext.Provider>
    </UserContext.Provider>
  );
}

export default App;