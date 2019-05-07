import boto3
import os

s3 = boto3.resource('s3')

directory = '/Users/bruceelgort/Desktop/Python/aws/images/'

if(os.path.exists(directory)):
    # iterate through each file
    for filename in os.listdir(directory):
        print('Uploading:',filename)
        s3.Bucket('saturday-academy').upload_file(directory + "/" + filename, filename)
        print('Uploaded',filename)

# Now list the bucket contents
for object in s3.Bucket('saturday-academy').objects.all():
    print(object.key)