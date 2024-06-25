import requests
import os

# GitHub token from environment variable
github_token = os.getenv('GITHUB_TOKEN_GITHUB_TOKEN')

def authenticate_github_token():
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    # Test the authentication by fetching the user's profile
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        print("User profile information:")
        print(response.json())
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")
        print(response.json())

if __name__ == '__main__':
    authenticate_github_token()
