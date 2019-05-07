import boto3
import os
from pprint import pprint

s3 = boto3.resource('s3')

file = '/Users/bruceelgort/Desktop/helloworld.txt'

if(os.path.exists(file)):
    filename = os.path.basename(file)
    s3.Bucket('saturday-academy').upload_file(file, 'helloworld.txt')
    print('Uploaded!')

for object in s3.Bucket('saturday-academy').objects.all():
    print(object)