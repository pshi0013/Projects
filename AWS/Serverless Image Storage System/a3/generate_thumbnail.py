import json
import numpy as np
import cv2
import boto3
import base64
import re

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
TABLE_NAME = "fit5225-pixtag-82"
BUCKET_NAME = "fit5225-82-s3"

def lambda_handler(event, context):
    # Extract the user ID from the event
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]

    # Get the uploaded image from the event
    image_data = base64.b64decode(event["image"])

    # Define the user-specific prefix in the bucket
    user_prefix = f"{user_id}/"

    # Create a key for the uploaded image using the user ID
    key = f"{user_prefix}image.jpg"

    upload_path = "/tmp/new_image.jpg"

    # Save the image to the /tmp directory
    with open(upload_path, "wb") as f:
        f.write(image_data)

    # Upload the image to the S3 bucket
    s3_client.upload_file(
        upload_path, BUCKET_NAME, key, ExtraArgs={"ACL": "public-read"}
    )

    print("File {0} uploaded to {1} bucket".format(key, BUCKET_NAME))

    # Read the image using OpenCV
    image = cv2.imread(upload_path)

    # Generate the thumbnail
    thumbnail = generate_thumbnail(image)

    # Save the thumbnail to a temporary file
    thumbnail_key = f"{user_prefix}image-thumb.jpg"
    thumbnail_path = f"/tmp/{thumbnail_key}"

    # Compression with quality=85
    cv2.imwrite(thumbnail_path, thumbnail, [cv2.IMWRITE_JPEG_QUALITY, 85])

    # Upload the thumbnail to S3 using the thumbnail_path directly
    s3_client.upload_file(
        thumbnail_path, BUCKET_NAME, thumbnail_key, ExtraArgs={"ACL": "public-read"}
    )

    # Generate URLs
    image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{key}"
    thumbnail_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{thumbnail_key}"

    # Insert to DynamoDB
    table = dynamodb.Table(TABLE_NAME)

    item = {
        "id": image_url,  # url in s3
        "ThumbnailURL": thumbnail_url,  # thumbnail url in s3
        "Tags": [],  # to be added in object_detection lambda
        "UserId": user_id,
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        "body": json.dumps({"filePath": image_url})
    }

def generate_thumbnail(image, size=(128, 128)):
    # Resize the image while maintaining aspect ratio
    h, w = image.shape[:2]
    scale = min(size[0] / w, size[1] / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # Resize the image
    resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Create a blank canvas with the desired thumbnail size
    thumbnail = np.zeros((size[1], size[0], 3), dtype=np.uint8)

    # Center the resized image on the canvas
    start_x = (size[0] - new_w) // 2
    start_y = (size[1] - new_h) // 2
    thumbnail[start_y : start_y + new_h, start_x : start_x + new_w] = resized_image

    return thumbnail