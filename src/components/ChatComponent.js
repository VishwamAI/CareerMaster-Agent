import React, { useState } from 'react';
import { Box, Input, Button, VStack, HStack, Text, Image } from '@chakra-ui/react';

const ChatComponent = () => {
  const [messages, setMessages] = useState([
    { text: 'Welcome to CareerMaster-Agent!', sender: 'system', timestamp: new Date().toLocaleTimeString() },
    { text: 'How can I assist you today?', sender: 'system', timestamp: new Date().toLocaleTimeString() },
    { text: 'I need help with my resume.', sender: 'user', timestamp: new Date().toLocaleTimeString() },
    { text: 'Sure, please upload your resume or provide your LinkedIn profile.', sender: 'system', timestamp: new Date().toLocaleTimeString() }
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, sender: 'user', timestamp: new Date().toLocaleTimeString() }]);
      setInput('');
      // Simulate a response from the system
      setTimeout(() => {
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: 'This is a response from the system.', sender: 'system', timestamp: new Date().toLocaleTimeString() },
        ]);
      }, 1000);
    }
  };

  return (
    <Box className="chat-container" p={4} bg="gray.100" borderRadius="md" boxShadow="md" display="flex">
      <Box className="sidebar" w="20%" p={4} bg="gray.200" borderRadius="md" boxShadow="md">
        <VStack spacing={4} align="stretch">
          <Button colorScheme="blue" variant="outline">Resume Creation</Button>
          <Button colorScheme="blue" variant="outline">Job Applying Agent</Button>
          <Button colorScheme="blue" variant="outline">Interview Updates</Button>
        </VStack>
      </Box>
      <Box className="chat-content" w="80%" p={4} bg="gray.100" borderRadius="md" boxShadow="md">
        <VStack spacing={4} align="stretch">
          <Box className="chat-messages" overflowY="auto" maxH="400px" p={2} bg="white" borderRadius="md" boxShadow="sm">
            {messages.map((message, index) => (
              <HStack
                key={index}
                justify={message.sender === 'user' ? 'flex-end' : 'flex-start'}
                animation="fadeIn 0.5s"
              >
                <Box className={`chat-bubble ${message.sender}`} p={4} bg={message.sender === 'user' ? 'blue.500' : 'gray.200'} color={message.sender === 'user' ? 'white' : 'black'} borderRadius="md" boxShadow="sm">
                  <Text>{message.text}</Text>
                  <Text fontSize="xs" color="gray.500">{message.timestamp}</Text>
                </Box>
              </HStack>
            ))}
          </Box>
          <HStack className="chat-input-container" spacing={3}>
            <Image
              src="./logo.png" // Replace with the actual path to the logo image
              alt="Logo"
              boxSize="50px"
              objectFit="cover"
              borderRadius="full"
              boxShadow="sm"
            />
            <Input
              className="chat-input"
              placeholder="Type your message..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => {
                if (e.key === 'Enter') handleSend();
              }}
              bg="white"
              borderRadius="md"
              boxShadow="sm"
            />
            <Button className="chat-send-button" onClick={handleSend} colorScheme="blue" borderRadius="md" boxShadow="sm">
              Send
            </Button>
          </HStack>
        </VStack>
      </Box>
    </Box>
  );
};

export default ChatComponent;
