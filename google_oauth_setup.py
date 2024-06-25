from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

def authenticate_google_oauth():
    # Set up the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'path/to/your/client_secret.json',
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )

    # Run the OAuth flow to obtain credentials
    credentials = flow.run_local_server(port=0)

    # Save the credentials for future use
    with open('token.json', 'w') as token_file:
        token_file.write(credentials.to_json())

    # Test the authentication by listing Google Cloud Storage buckets
    service = build('storage', 'v1', credentials=credentials)
    request = service.buckets().list(project='your-google-cloud-project-id')
    response = request.execute()

    print("Buckets in Google Cloud Storage:")
    for bucket in response.get('items', []):
        print(bucket['name'])

if __name__ == '__main__':
    authenticate_google_oauth()
