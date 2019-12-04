import boto3


def smt(self):
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id="AKIAJWQSMVAJ5T4YHFTA",
        aws_secret_access_key="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",
        region_name="us-east-1"
    )

    # Create the topic if it doesn't exist (this is important)
    #topic = client.create_topic(Name="SM_team")
    #topic_arn = topic['arn:aws:sns:us-east-1:927659535410:SM_team']   # Get it's Amazon Resource Name

    # Add SMS Subscribers

    some_list_of_contacts = ['+918087024591', '+918451044751', '+918879080168', '+919867603337']

    for number in some_list_of_contacts:
        client.subscribe(
            TopicArn="arn:aws:sns:us-east-1:927659535410:SM_team",
            Protocol='sms',
            Endpoint=number  # <-- number who'll receive an SMS message.
        )

    # Publish a message.
    client.publish(Message="This is demo testing for sending SMS notifications to Sales and Marketing staff for optician registration.", TopicArn="arn:aws:sns:us-east-1:927659535410:SM_team")
