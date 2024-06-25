import React from 'react';
import { ChakraProvider, Box, Flex, Heading, Text, Link } from '@chakra-ui/react';
import './App.css';

function App() {
  return (
    <ChakraProvider>
      <Flex direction="column" minH="100vh">
        <Box as="header" bg="teal.500" color="white" py={4}>
          <Heading as="h1" size="lg" textAlign="center">
            CareerMaster-Agent
          </Heading>
        </Box>
        <Box as="main" flex="1" p={4}>
          <Text fontSize="xl" textAlign="center">
            Welcome to CareerMaster-Agent! Your automated job application assistant.
          </Text>
        </Box>
        <Box as="footer" bg="teal.500" color="white" py={4} textAlign="center">
          <Text>&copy; 2024 CareerMaster-Agent. All rights reserved.</Text>
        </Box>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
