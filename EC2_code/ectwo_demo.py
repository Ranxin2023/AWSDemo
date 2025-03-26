import boto3
from dotenv import load_dotenv
import os
load_dotenv()
ec2 = boto3.resource('ec2', region_name='us-east-1')

# Launch a new EC2 instance
instances = ec2.create_instances(
    ImageId=os.getenv("ImageId"),  # Replace with a real AMI ID in your region
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName=os.getenv("keyName"),     # Replace with your EC2 key pair name
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyTestInstance'}]
        }
    ]
)

print("Launched EC2 Instance with ID:", instances[0].id)
