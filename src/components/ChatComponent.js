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
    <Box
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      p={4}
      bg="white"
      boxShadow="md"
      maxW="md"
      mx="auto"
      mt={4}
    >
      <VStack spacing={4} align="stretch">
        <Box
          borderWidth="1px"
          borderRadius="lg"
          overflow="hidden"
          p={4}
          bg="gray.50"
          h="300px"
          overflowY="auto"
        >
          {messages.map((message, index) => (
            <HStack
              key={index}
              justify={message.sender === 'user' ? 'flex-end' : 'flex-start'}
            >
              <Box
                bg={message.sender === 'user' ? 'blue.500' : 'gray.300'}
                color={message.sender === 'user' ? 'white' : 'black'}
                px={4}
                py={2}
                borderRadius="md"
                maxW="80%"
              >
                <Text>{message.text}</Text>
              </Box>
            </HStack>
          ))}
        </Box>
        <HStack>
          <Input
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter') handleSend();
            }}
          />
          <Button onClick={handleSend} colorScheme="blue">
            Send
          </Button>
        </HStack>
      </VStack>
    </Box>
  );
};

export default ChatComponent;
