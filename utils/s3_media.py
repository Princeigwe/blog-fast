import boto3

s3_client = boto3.resource(
  's3',
  aws_access_key_id = "test_access_key",
  aws_secret_access_key = "test_secret_key"
)

def list_buckets():
  return [bucket.name for bucket in s3_client.buckets.all()]


def create_bucket():
  bucket_name = "test-bucket"
  existing_buckets = list_buckets()

  if bucket_name in existing_buckets:
    return bucket_name
  
  s3_client.create_bucket(
    ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
    Bucket=bucket_name,
  )
  return bucket_name


def media_upload(file_name, file_content):
  s3_bucket = create_bucket()
  try:
    response = s3_client.Bucket(s3_bucket).put_object(Key=file_name, Body=file_content)
    return response
  except Exception as e:
    return e