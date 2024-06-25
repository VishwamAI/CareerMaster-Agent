from google.cloud import storage
import os

def authenticate_google_cloud():
    # Check for environment variables
    google_cloud_project_id = os.getenv('PROJECT')
    google_application_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

    if not google_cloud_project_id or not google_application_credentials:
        print("Error: Google Cloud project ID or service account JSON key file path not set in environment variables.")
        return

    # Set up Google Cloud authentication using environment variables
    os.environ['GOOGLE_CLOUD_PROJECT'] = google_cloud_project_id
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_application_credentials

    # Initialize the Google Cloud Storage client
    client = storage.Client()

    # Test the authentication by listing buckets
    buckets = list(client.list_buckets())
    print("Buckets in Google Cloud Storage:")
    for bucket in buckets:
        print(bucket.name)

if __name__ == '__main__':
    authenticate_google_cloud()
