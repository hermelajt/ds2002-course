import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2002-sgm3pm'

# PRIVATE upload
s3.upload_file('public-cloud.jpg', bucket, 'private-file.jpg')

print("Private upload complete")

# PUBLIC upload
s3.upload_file(
    'public-cloud.jpg',
    bucket,
    'public-file.jpg',
    ExtraArgs={'ACL': 'public-read'}
)

print("Public upload complete")
