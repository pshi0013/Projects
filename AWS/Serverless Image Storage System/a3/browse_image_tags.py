# import json
# import boto3
# from boto3.dynamodb.conditions import Attr, And
#
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('fit5225-82-pixtag-dynamodb')
#
# def lambda_handler(event, context):
#     print(f"Event: {json.dumps(event)}")  # Log the incoming event
#     tags_query = event.get('queryStringParameters', {}).get('tags', '')
#     print(f"Tags Query: {tags_query}")
#     if tags_query:
#         tags_list = tags_query.split(',')
#         response = search_images(tags_list)
#     else:
#         response = {'links': []}
#
#     print(f"Response: {json.dumps(response)}")  # Log the response
#
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Credentials': True
#         },
#         'body': json.dumps(response)
#     }
#
# def parse_tags(tags_list):
#     tag_count = {}
#     for tag in tags_list:
#         if tag.isdigit():
#             continue
#         count = 1
#         idx = tags_list.index(tag) + 1
#         if idx < len(tags_list) and tags_list[idx].isdigit():
#             count = int(tags_list[idx])
#         if tag in tag_count:
#             tag_count[tag] += count
#         else:
#             tag_count[tag] = count
#     return tag_count
#
# def search_images(tags_list):
#     tag_count = parse_tags(tags_list)
#     filter_expression = None
#     for tag, count in tag_count.items():
#         tag_filter = Attr('Tags').contains({'label': tag})
#         for _ in range(1, count):
#             tag_filter = And(tag_filter, Attr('Tags').contains({'label': tag}))
#         if filter_expression is None:
#             filter_expression = tag_filter
#         else:
#             filter_expression = And(filter_expression, tag_filter)
#
#     if filter_expression:
#         response = table.scan(FilterExpression=filter_expression)
#         items = response.get('Items', [])
#         links = [item['ThumbnailURL'] for item in items]
#         return {'links': links}
#     else:
#         return {'links': []}
#
#     import json
#     import boto3
#     from boto3.dynamodb.conditions import Attr, And
#
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('fit5225-pixtag-82')
#
#     def lambda_handler(event, context):
#         print(f"Event: {json.dumps(event)}")  # Log the incoming event
#
#         try:
#             # Extract the user ID from the event
#             user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
#             print(f"User ID: {user_id}")
#
#             # Extract query parameters
#             tags_query = event.get('queryStringParameters', {}).get('tags', '')
#             print(f"Tags Query: {tags_query}")
#
#             if tags_query:
#                 tags_list = tags_query.split(',')
#                 response = search_images(tags_list, user_id)
#             else:
#                 response = {'links': []}
#
#             print(f"Response: {json.dumps(response)}")  # Log the response
#
#             return {
#                 'statusCode': 200,
#                 'headers': {
#                     'Access-Control-Allow-Origin': '*',
#                     'Access-Control-Allow-Credentials': True
#                 },
#                 'body': json.dumps(response)
#             }
#         except Exception as e:
#             print(f"Error: {str(e)}")
#             return {
#                 'statusCode': 500,
#                 'headers': {
#                     'Access-Control-Allow-Origin': '*',
#                     'Access-Control-Allow-Credentials': True
#                 },
#                 'body': json.dumps({'message': str(e)})
#             }
#
#     def parse_tags(tags_list):
#         tag_count = {}
#         for tag in tags_list:
#             if tag.isdigit():
#                 continue
#             count = 1
#             idx = tags_list.index(tag) + 1
#             if idx < len(tags_list) and tags_list[idx].isdigit():
#                 count = int(tags_list[idx])
#             if tag in tag_count:
#                 tag_count[tag] += count
#             else:
#                 tag_count[tag] = count
#         return tag_count
#
#     def search_images(tags_list, user_id):
#         tag_count = parse_tags(tags_list)
#         filter_expression = Attr('UserId').eq(user_id)
#
#         for tag, count in tag_count.items():
#             tag_filter = Attr('Tags').contains({'label': tag})
#             for _ in range(1, count):
#                 tag_filter = And(tag_filter, Attr('Tags').contains({'label': tag}))
#             filter_expression = And(filter_expression, tag_filter)
#
#         response = table.scan(FilterExpression=filter_expression)
#         items = response.get('Items', [])
#         links = [item['ThumbnailURL'] for item in items]
#         return {'links': links}


# import json
# import boto3
# from boto3.dynamodb.conditions import Attr, And
#
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('fit5225-pixtag-82')
#
#
# def lambda_handler(event, context):
#     print(f"Event: {json.dumps(event)}")  # Log the incoming event
#
#     try:
#         # Extract the user ID from the event
#         user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
#         print(f"User ID: {user_id}")
#
#         # Extract query parameters
#         tags_query = event.get('queryStringParameters', {}).get('tags', '')
#         print(f"Tags Query: {tags_query}")
#
#         if tags_query:
#             tags_list = tags_query.split(',')
#             response = search_images(tags_list, user_id)
#         else:
#             response = {'links': []}
#
#         print(f"Response: {json.dumps(response)}")  # Log the response
#
#         return {
#             'statusCode': 200,
#             'headers': {
#                 'Access-Control-Allow-Origin': '*',
#                 'Access-Control-Allow-Credentials': True
#             },
#             'body': json.dumps(response)
#         }
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return {
#             'statusCode': 500,
#             'headers': {
#                 'Access-Control-Allow-Origin': '*',
#                 'Access-Control-Allow-Credentials': True
#             },
#             'body': json.dumps({'message': str(e)})
#         }
#
#
# def parse_tags(tags_list):
#     tag_count = {}
#     for tag in tags_list:
#         if tag.isdigit():
#             continue
#         count = 1
#         idx = tags_list.index(tag) + 1
#         if idx < len(tags_list) and tags_list[idx].isdigit():
#             count = int(tags_list[idx])
#         if tag in tag_count:
#             tag_count[tag] += count
#         else:
#             tag_count[tag] = count
#     return tag_count
#
#
# def search_images(tags_list, user_id):
#     tag_count = parse_tags(tags_list)
#     filter_expression = Attr('UserId').eq(user_id)
#
#     for tag, count in tag_count.items():
#         tag_filter = Attr('Tags').contains({'label': tag})
#         for _ in range(1, count):
#             tag_filter = And(tag_filter, Attr('Tags').contains({'label': tag}))
#         filter_expression = And(filter_expression, tag_filter)
#
#     response = table.scan(FilterExpression=filter_expression)
#     items = response.get('Items', [])
#     links = [item['ThumbnailURL'] for item in items]
#     return {'links': links}


import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fit5225-pixtag-82')


def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")  # Log the incoming event

    try:
        # Extract the user ID from the event
        user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        print(f"User ID: {user_id}")

        # Extract query parameters
        tags_query = event.get('queryStringParameters', {}).get('tags', '')
        print(f"Tags Query: {tags_query}")

        if tags_query:
            tags_list = tags_query.replace(" ", "").split(',')
            response = search_images(tags_list, user_id)
        else:
            response = {'links': []}

        print(f"Response: {json.dumps(response)}")  # Log the response

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(response)
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'message': str(e)})
        }


def parse_tags(tags_list):
    tag_count = {}
    i = 0
    while i < len(tags_list):
        tag = tags_list[i]
        if tag.isdigit():
            i += 1
            continue
        count = 1
        if i + 1 < len(tags_list) and tags_list[i + 1].isdigit():
            count = int(tags_list[i + 1])
            i += 1
        if tag in tag_count:
            tag_count[tag] += count
        else:
            tag_count[tag] = count
        i += 1
    return tag_count


def search_images(tags_list, user_id):
    tag_count = parse_tags(tags_list)  # Assuming you have a working implementation for this
    filter_expression = Attr('UserId').eq(user_id)

    for tag, count in tag_count.items():
        tag_filter = Attr('Tags').contains({'label': tag})
        filter_expression = filter_expression & tag_filter

    response = table.scan(FilterExpression=filter_expression)
    items = response.get('Items', [])

    filtered_items = []
    for item in items:
        item_tags = item.get('Tags', [])
        tag_occurrences = sum(1 for t in item_tags if t['label'] == tag)
        if tag_occurrences >= count:
            filtered_items.append(item)

    links = [item['ThumbnailURL'] for item in filtered_items]
    return {'links': links}