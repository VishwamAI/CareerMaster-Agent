import requests
import os
from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

# GitHub OAuth settings
GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')
GITHUB_REDIRECT_URI = 'http://localhost:5000/github/callback'
GITHUB_AUTH_URL = 'https://github.com/login/oauth/authorize'
GITHUB_TOKEN_URL = 'https://github.com/login/oauth/access_token'
GITHUB_USER_URL = 'https://api.github.com/user'

@app.route('/github')
def github_login():
    auth_url = f"{GITHUB_AUTH_URL}?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_REDIRECT_URI}&scope=user"
    return redirect(auth_url)

@app.route('/github/callback')
def github_callback():
    code = request.args.get('code')
    token_response = requests.post(GITHUB_TOKEN_URL, headers={'Accept': 'application/json'}, data={
        'client_id': GITHUB_CLIENT_ID,
        'client_secret': GITHUB_CLIENT_SECRET,
        'code': code,
        'redirect_uri': GITHUB_REDIRECT_URI
    })
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    user_response = requests.get(GITHUB_USER_URL, headers={
        'Authorization': f'token {access_token}'
    })
    user_json = user_response.json()

    return f"User profile information: {user_json}"

if __name__ == '__main__':
    app.run(debug=True)
