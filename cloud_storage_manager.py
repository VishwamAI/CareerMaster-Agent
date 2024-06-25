from google.cloud import storage
import os

def create_bucket(bucket_name):
    """Creates a new bucket in Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    if not bucket.exists():
        bucket = client.create_bucket(bucket_name)
        print(f"Bucket {bucket_name} created.")
    else:
        print(f"Bucket {bucket_name} already exists.")
    return bucket

def upload_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def download_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a file from the bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def list_files(bucket_name):
    """Lists all the blobs in the bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    print(f"Files in bucket {bucket_name}:")
    for blob in blobs:
        print(blob.name)

if __name__ == '__main__':
    # Example usage
    bucket_name = 'your-bucket-name'
    create_bucket(bucket_name)
    upload_file(bucket_name, 'path/to/local/file', 'destination_blob_name')
    download_file(bucket_name, 'source_blob_name', 'path/to/local/destination/file')
    list_files(bucket_name)
