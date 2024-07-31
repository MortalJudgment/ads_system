import React, { useContext } from 'react';
import { UserContext } from '../../contexts/UserContext';
import { ChatContext } from '../../contexts/ChatContext';
import ChatWindow from './ChatWindow';
import MessageInput from './MessageInput';
import AdDisplay from '../AdDisplay/AdDisplay';
import './ChatApp.css';

function ChatApp() {
  const { user } = useContext(UserContext);
  const { chatMessages, setChatMessages } = useContext(ChatContext);

  const handleSendMessage = (message) => {
    // Here you would typically send the message to your backend
    // and handle the response from the multi-agent system
    setChatMessages([...chatMessages, { sender: 'user', text: message }]);
  };

  return (
    <div className="chat-app">
      <div className="chat-container">
        <ChatWindow messages={chatMessages} />
        <MessageInput onSendMessage={handleSendMessage} />
      </div>
      <AdDisplay userInterests={user.interests} />
    </div>
  );
}

export default ChatApp;