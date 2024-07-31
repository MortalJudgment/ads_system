import { useState, useEffect, useContext } from 'react';
import { UserContext } from '../contexts/UserContext';
import { ChatContext } from '../contexts/ChatContext';
import { sendMessage } from '../services/api';

export function useChat() {
  const { user } = useContext(UserContext);
  const { chatMessages, setChatMessages } = useContext(ChatContext);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // You could potentially load previous messages here
  }, []);

  const sendChatMessage = async (message) => {
    setIsLoading(true);
    try {
      const newUserMessage = { sender: 'user', text: message };
      setChatMessages(prev => [...prev, newUserMessage]);

      const response = await sendMessage(user.id, message);
      const newAgentMessage = { sender: 'agent', text: response.message };
      setChatMessages(prev => [...prev, newAgentMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      // Handle error (e.g., show an error message to the user)
    } finally {
      setIsLoading(false);
    }
  };

  return { chatMessages, sendChatMessage, isLoading };
}