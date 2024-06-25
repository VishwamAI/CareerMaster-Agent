from google.cloud import storage
import os

def create_bucket(bucket_name):
    """Creates a new bucket in Google Cloud Storage."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        if not bucket.exists():
            bucket = client.create_bucket(bucket_name)
            print(f"Bucket {bucket_name} created.")
        else:
            print(f"Bucket {bucket_name} already exists.")
        return bucket
    except Exception as e:
        print(f"Error creating bucket {bucket_name}: {e}")

def upload_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        print(f"Error uploading file {source_file_name} to {destination_blob_name}: {e}")

def download_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a file from the bucket."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
    except Exception as e:
        print(f"Error downloading blob {source_blob_name} to {destination_file_name}: {e}")

def list_files(bucket_name):
    """Lists all the blobs in the bucket."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blobs = bucket.list_blobs()
        print(f"Files in bucket {bucket_name}:")
        for blob in blobs:
            print(blob.name)
    except Exception as e:
        print(f"Error listing files in bucket {bucket_name}: {e}")

def delete_file(bucket_name, blob_name):
    """Deletes a file from the bucket."""
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()
        print(f"Blob {blob_name} deleted from bucket {bucket_name}.")
    except Exception as e:
        print(f"Error deleting blob {blob_name} from bucket {bucket_name}: {e}")

if __name__ == '__main__':
    # Example usage
    bucket_name = 'your-bucket-name'
    create_bucket(bucket_name)
    upload_file(bucket_name, 'path/to/local/file', 'destination_blob_name')
    download_file(bucket_name, 'source_blob_name', 'path/to/local/destination/file')
    list_files(bucket_name)
    delete_file(bucket_name, 'blob_name_to_delete')
