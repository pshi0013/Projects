import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fit5225-82-pixtag-dynamodb')


def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")  # Log the incoming event

    tags_query = event["queryStringParameters"]["tags"]
    urls_query = event["queryStringParameters"]["urls"]
    action = str(event["queryStringParameters"]["action"])

    print(f"Tags Query: {tags_query}")
    print(f"URLs Query: {urls_query}")
    print(f"Action: {action}")

    if tags_query and urls_query and action:
        response = update_tags(urls_query, action, tags_query)
    else:
        response = "No update performed."

    print(f"Response: {json.dumps(response)}")  # Log the response

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(response)
    }


def get_image_by_url(thumbnail_url):
    response = table.scan(FilterExpression=Attr("ThumbnailURL").eq(thumbnail_url))
    items = response["Items"]
    if items:
        return items[0]["id"]
    return None


def update_tags(urls, action_type, tags):
    for url in urls:
        image_url = get_image_by_url(url)
        if not image_url:
            continue  # Skip if the image URL does not exist

        # Fetch the existing tags
        response = table.get_item(Key={"id": image_url})
        existing_tags = response.get("Item", {}).get("Tags", [])

        if action_type == "1":  # Add tags
            # Ensure no duplicate tags are added
            new_tags = [{"label": tag} for tag in tags if {"label": tag} not in existing_tags]
            updated_tags = existing_tags + new_tags
            update_expression = "SET Tags = :updated_tags"
            expression_attribute_values = {":updated_tags": updated_tags}
        else:  # Remove tags
            # Remove specified tags
            updated_tags = [tag for tag in existing_tags if tag["label"] not in tags]
            update_expression = "SET Tags = :updated_tags"
            expression_attribute_values = {":updated_tags": updated_tags}

        table.update_item(
            Key={"id": image_url},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )

    return "Tags updated successfully"

