import boto3

s3 = boto3.resource('s3')

s3.create_bucket(Bucket='bruceelgort22',CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})
print('Bucket created!')