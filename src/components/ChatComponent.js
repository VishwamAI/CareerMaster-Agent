import React, { useState } from 'react';
import { Box, Input, Button, VStack, HStack, Text } from '@chakra-ui/react';

const ChatComponent = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, sender: 'user' }]);
      setInput('');
      // Simulate a response from the system
      setTimeout(() => {
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: 'This is a response from the system.', sender: 'system' },
        ]);
      }, 1000);
    }
  };

  return (
    <Box className="chat-container">
      <VStack spacing={4} align="stretch">
        <Box className="chat-messages">
          {messages.map((message, index) => (
            <HStack
              key={index}
              justify={message.sender === 'user' ? 'flex-end' : 'flex-start'}
            >
              <Box className={`chat-bubble ${message.sender}`}>
                <Text>{message.text}</Text>
              </Box>
            </HStack>
          ))}
        </Box>
        <HStack className="chat-input-container">
          <Input
            className="chat-input"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter') handleSend();
            }}
          />
          <Button className="chat-send-button" onClick={handleSend}>
            Send
          </Button>
        </HStack>
      </VStack>
    </Box>
  );
};

export default ChatComponent;
