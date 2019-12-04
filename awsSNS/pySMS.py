import boto3

# Create an SNS client

client = boto3.client(
    "sns",
    aws_access_key_id="AKIAJWQSMVAJ5T4YHFTA",
    aws_secret_access_key="W5WL3kMhuTf5Oht+kozgM7cjvTAWfA74GCy6IyVu",
    region_name="us-east-1"
)

# Send your sms message.

client.publish(
    PhoneNumber="+918087024591",
    Message="This is a test message for sending sms to a Phone number using aws SNS(Simple Notification Service)."

)