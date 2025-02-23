import json
import base64
import boto3
import cv2
import numpy as np
from boto3.dynamodb.conditions import Attr, And

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fit5225-82-pixtag-dynamodb')

def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")  # Log the incoming event

    # Step 1: Decode the base64 image
    image_data = base64.b64decode(event["image"])
    image_np = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    # Step 2: Load YOLO model and config files
    label_path = "/tmp/coco.names"
    weight_path = "/tmp/yolov3-tiny.weights"
    cfg_path = "/tmp/yolov3-tiny.cfg"

    config_bucket = "venus-0529"

    # Download the configuration files from S3
    s3_client.download_file(config_bucket, "yolo_tiny_configs/coco.names", label_path)
    s3_client.download_file(config_bucket, "yolo_tiny_configs/yolov3-tiny.weights", weight_path)
    s3_client.download_file(config_bucket, "yolo_tiny_configs/yolov3-tiny.cfg", cfg_path)

    Labels = get_labels(label_path)

    # Step 3: Detect objects using YOLO
    net = load_model(cfg_path, weight_path)
    objects_list = do_prediction(image, net, Labels)
    detected_tags = [obj['label'] for obj in objects_list]

    # Step 4: Retrieve images from DynamoDB that match the detected tags
    response = search_images_by_tags(detected_tags)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'links': response['links'], 'tags': detected_tags})
    }

def get_labels(labels_path):
    with open(labels_path, 'r') as file:
        labels = file.read().strip().split("\n")
    return labels

def load_model(configpath, weightspath):
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net

def do_prediction(image, net, LABELS):
    (H, W) = image.shape[:2]
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)

    boxes = []
    confidences = []
    classIDs = []

    confthres = 0.3
    nmsthres = 0.1

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > confthres:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres, nmsthres)
    objects_list = []

    if len(idxs) > 0:
        for i in idxs.flatten():
            label = LABELS[classIDs[i]]
            obj = {'label': label}
            objects_list.append(obj)

    return objects_list

def search_images_by_tags(tags_list):
    filter_expression = None
    for tag in tags_list:
        tag_filter = Attr('Tags').contains({'label': tag})
        if filter_expression is None:
            filter_expression = tag_filter
        else:
            filter_expression = And(filter_expression, tag_filter)

    if filter_expression:
        response = table.scan(FilterExpression=filter_expression)
        items = response.get('Items', [])
        links = [item['ThumbnailURL'] for item in items]
        return {'links': links}
    else:
        return {'links': []}
