from google.cloud import storage
import os

def authenticate_google_cloud():
    # Set up Google Cloud authentication using environment variables
    os.environ['GOOGLE_CLOUD_PROJECT'] = 'your-google-cloud-project-id'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/path/to/your/service-account-file.json'

    # Initialize the Google Cloud Storage client
    client = storage.Client()

    # Test the authentication by listing buckets
    buckets = list(client.list_buckets())
    print("Buckets in Google Cloud Storage:")
    for bucket in buckets:
        print(bucket.name)

if __name__ == '__main__':
    authenticate_google_cloud()
