import json
import boto3

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = "fit5225-pixtag-82"


def lambda_handler(event, context):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]

    table = dynamodb.Table(TABLE_NAME)

    response = table.scan(
        FilterExpression="UserId = :user_id",
        ExpressionAttributeValues={":user_id": user_id}
    )

    images = response.get("Items", [])

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps(images)
    }
