import React from 'react';
import { ChakraProvider, Box, Flex, Heading, Text, Button, Image } from '@chakra-ui/react';
import { FaBriefcase, FaLinkedin, FaGithub } from 'react-icons/fa';
import './App.css';
import ChatComponent from './components/ChatComponent';

function App() {
  return (
    <ChakraProvider>
      <Flex direction="column" minH="100vh">
        <Box as="header" bg="teal.500" color="white" py={4}>
          <Heading as="h1" size="lg" textAlign="center">
            CareerMaster-Agent
          </Heading>
        </Box>
        <Box as="main" flex="1" p={4} textAlign="center">
          <Image src="https://via.placeholder.com/150" alt="Job Search" mx="auto" mb={4} />
          <Text fontSize="xl" fontWeight="bold">
            Welcome to CareerMaster-Agent! Your automated job application assistant.
          </Text>
          <Button mt={4} colorScheme="teal" size="lg" leftIcon={<FaBriefcase />}>
            Get Started
          </Button>
          <ChatComponent />
        </Box>
        <Box as="footer" bg="teal.500" color="white" py={4} textAlign="center">
          <Text>&copy; 2024 CareerMaster-Agent. All rights reserved.</Text>
          <Flex justify="center" mt={2}>
            <Button as="a" href="https://www.linkedin.com" target="_blank" colorScheme="linkedin" mx={2} leftIcon={<FaLinkedin />}>
              LinkedIn
            </Button>
            <Button as="a" href="https://www.github.com" target="_blank" colorScheme="gray" mx={2} leftIcon={<FaGithub />}>
              GitHub
            </Button>
          </Flex>
        </Box>
      </Flex>
    </ChakraProvider>
  );
}

export default App;
