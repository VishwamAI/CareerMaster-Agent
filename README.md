# CareerMaster-Agent

The CareerMaster-Agent is an automated job application system designed to streamline the job search process. It automates the creation of ATS-compliant resumes, applies for jobs on various platforms, and manages interview updates within the platform.

## Features
1. User Authentication: Supports login/signup with Google, LinkedIn, and GitHub OAuth.
2. Resume Creation: Generates ATS-compliant resumes from LinkedIn profiles or user-uploaded resumes.
3. Job Applications: Automatically applies for jobs on LinkedIn and other job platforms.
4. Notifications: Notifies users upon successful job applications and interview updates.
5. Cloud Storage: Utilizes Google Cloud Storage for storing user data.

## Getting Started

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Prerequisites
- Node.js
- npm
- Google Cloud account
- LinkedIn, GitHub, and Google OAuth credentials

### Available Scripts

In the project directory, you can run:

#### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

#### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

#### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

#### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Project Setup

### Google Cloud Setup
1. Create a Google Cloud project.
2. Enable the Google Cloud Storage API.
3. Create a service account and download the JSON key file.
4. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON key file.

### OAuth Setup
1. Create OAuth credentials for Google, LinkedIn, and GitHub.
2. Set the following environment variables:
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`
   - `LINKEDIN_CLIENT_ID`
   - `LINKEDIN_CLIENT_SECRET`
   - `GITHUB_CLIENT_ID`
   - `GITHUB_CLIENT_SECRET`

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
