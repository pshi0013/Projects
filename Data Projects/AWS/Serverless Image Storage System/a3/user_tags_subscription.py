import json
import boto3
import jwt
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
sns_client = boto3.client('sns')
TABLE_NAME = 'UserNotificationConfiguration'

# Replace this URL with your Cognito User Pool URL
COGNITO_USER_POOL_URL = "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_Dyyz6kNcG"

def lambda_handler(event, context):
    try:
        # Extract the idToken from the headers
        id_token = event['headers'].get('Authorization', '').split(' ')[1]
        print(f"ID Token: {id_token}")

        # Decode the ID token to get user info
        user_info = jwt.decode(id_token, options={"verify_signature": False})
        email = user_info.get('email')
        print(f"User Email: {email}")

        body = json.loads(event['body'])
        new_tags = body['tags']
        print(f"New Tags: {new_tags}")

        # Save subscription to DynamoDB and get old tags
        table = dynamodb.Table(TABLE_NAME)
        response = table.get_item(Key={'email': email})
        old_tags = response.get('Item', {}).get('tags', [])
        print(f"Old Tags: {old_tags}")

        # Unsubscribe from old tags
        for tag in old_tags:
            topic_name = f"ImageTag_{tag}"
            topic_arn = sns_client.create_topic(Name=topic_name)['TopicArn']
            subscriptions = sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)['Subscriptions']
            for subscription in subscriptions:
                if subscription['Endpoint'] == email:
                    sns_client.unsubscribe(SubscriptionArn=subscription['SubscriptionArn'])
                    print(f"Unsubscribed {email} from topic {topic_name}")

        # Update DynamoDB with new tags
        table.put_item(Item={'email': email, 'tags': new_tags})
        print("Updated subscription in DynamoDB")

        # Subscribe to new tags
        for tag in new_tags:
            topic_name = f"ImageTag_{tag}"
            topic_arn = sns_client.create_topic(Name=topic_name)['TopicArn']
            sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol='email',
                Endpoint=email
            )
            print(f"Subscribed {email} to topic {topic_name}")

            # Send confirmation message to the user
            confirmation_message = f"You have subscribed to the tag: {tag}"
            sns_client.publish(
                TopicArn=topic_arn,
                Message=json.dumps({
                    "default": confirmation_message
                }),
                Subject="Subscription Confirmation",
                MessageStructure='json'
            )
            print(f"Sent subscription confirmation message to topic {topic_name}")

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps('Subscription successful')
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(f"Subscription failed: {str(e)}")
        }
