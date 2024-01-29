import boto3 
import os
os.environ["LOCALSTACK_HOSTNAME"] = "localhost"
os.environ["USE_SSL"] = "false"
# import time
# time.sleep(5)

# Create a client for S3
s3 = boto3.client(
    's3', 
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test', 
    aws_secret_access_key='test',
    region_name='us-east-1'
)


print("Creating S3 client...")

try:
    # Create a bucket
    s3.create_bucket(Bucket='my-bucket')
    print("Bucket 'my-bucket' created successfully.")
except Exception as e:
    print(f"Error creating bucket: {e}")

try: 
    # Upload a file to the bucket
    s3.upload_file('my-file.txt', 'my-bucket', 'my-file.txt')
    print("File 'my-file.txt' uploaded to 'my-bucket'.")
except Exception as e:
    print(f"Error uploading file: {e}")

try:
    # List the objects in the bucket
    objects = s3.list_objects(Bucket='my-bucket')
    print("Objects in 'my-bucket':")
    if 'Contents' in objects:
        for object in objects['Contents']:
            print(object['Key'])
    else:
        print("No objects in bucket.")
except Exception as e:
    print(f"Error listing objects: {e}")

try:
    #Delete all objects in the bucket
    objects = s3.list_objects(Bucket='my-bucket')
    if 'Contents' in objects:
        for obj in objects['Contents']:
            s3.delete_object(Bucket='my-bucket', Key=obj['Key'])
        print("All objects in 'my-bucket' deleted.")
    else:
        print("Bucket is already empty.")
    # Delete the bucket (only empty buckets can be deleted)
    s3.delete_bucket(Bucket='my-bucket')
    print("Bucket 'my-bucket' deleted successfully.")
except Exception as e:
    print(f"Error deleting bucket: {e}")


# print('Hello world')