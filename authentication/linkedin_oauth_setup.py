import requests
import os
from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

# LinkedIn OAuth settings
LINKEDIN_CLIENT_ID = '86jwmes8cqsua0'
LINKEDIN_CLIENT_SECRET = 'gaICAyUcnVcRuYj0'
LINKEDIN_REDIRECT_URI = 'http://localhost:5000/callback'
LINKEDIN_AUTH_URL = 'https://www.linkedin.com/oauth/v2/authorization'
LINKEDIN_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'
LINKEDIN_PROFILE_URL = 'https://api.linkedin.com/v2/me'

@app.route('/')
def index():
    return '<a href="/login">Login with LinkedIn</a>'

@app.route('/login')
def login():
    auth_url = f"{LINKEDIN_AUTH_URL}?response_type=code&client_id={LINKEDIN_CLIENT_ID}&redirect_uri={LINKEDIN_REDIRECT_URI}&scope=r_liteprofile%20r_emailaddress"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_response = requests.post(LINKEDIN_TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': LINKEDIN_REDIRECT_URI,
        'client_id': LINKEDIN_CLIENT_ID,
        'client_secret': LINKEDIN_CLIENT_SECRET
    })
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    profile_response = requests.get(LINKEDIN_PROFILE_URL, headers={
        'Authorization': f'Bearer {access_token}'
    })
    profile_json = profile_response.json()

    return f"User profile information: {profile_json}"

if __name__ == '__main__':
    app.run(debug=True)
