import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB and S3 clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table('fit5225-82-pixtag-dynamodb')
bucket_name = 'fit5225-82-s3'


def lambda_handler(event, context):
    try:
        # Extract image ID from query string parameters
        image_id = event['queryStringParameters']['id']

        # Logging the image_id
        print(f"Deleting image with ID: {image_id}")

        # Delete item from DynamoDB
        response = table.delete_item(
            Key={
                'id': image_id
            }
        )

        # Check if the item was successfully deleted from DynamoDB
        if response.get('ResponseMetadata').get('HTTPStatusCode') == 200:
            # Parse the image URL to get the S3 key
            s3_key = image_id.split("/")[-1]

            # Logging the S3 key
            print(f"S3 Key for deletion: {s3_key}")

            # Delete the image from S3
            s3.delete_object(Bucket=bucket_name, Key=s3_key)
            s3.delete_object(Bucket=bucket_name, Key=s3_key.replace(".jpg", "-thumb.jpg"))

            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps({'message': 'Image deleted successfully'})
            }
        else:
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Credentials': True
                },
                'body': json.dumps({'message': 'Failed to delete image from DynamoDB'})
            }
    except ClientError as e:
        print(f"ClientError: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'message': str(e)})
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'message': str(e)})
        }
