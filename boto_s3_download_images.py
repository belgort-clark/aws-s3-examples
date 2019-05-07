# boto_s3_download_images.py

import boto3
import botocore

s3 = boto3.resource('s3')

# local folder to download images to
directory = '/Users/bruceelgort/Desktop/Python/aws/images_from_s3/'

try:
    for object in s3.Bucket('saturday-academy').objects.all():
        print('Downloading:', object.key)
        s3.Bucket('saturday-academy').download_file(object.key, directory + "/" + object.key, )
        print('Downloaded:', object.key)
except botocore.exceptions.ClientError as e:
    print(e.response['Error']['Code'])
except:
    print('Something went wrong')
