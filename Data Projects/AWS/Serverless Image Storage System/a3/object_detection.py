import json
import numpy as np
import cv2
import boto3
import base64

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
sns_client = boto3.client("sns")

TABLE_NAME = "fit5225-82-pixtag-dynamodb"
BUCKET_NAME = "fit5225-82-s3"


def lambda_handler(event, context):
    get_last_modified = lambda obj: int(obj["LastModified"].strftime("%s"))
    objs = s3_client.list_objects_v2(Bucket=BUCKET_NAME)["Contents"]
    latest_object = sorted(objs, key=get_last_modified, reverse=True)[1]
    object_key = latest_object["Key"]

    if "thumb" not in object_key:
        label_path = "/tmp/coco.names"
        weight_path = "/tmp/yolov3-tiny.weights"
        cfg_path = "/tmp/yolov3-tiny.cfg"

        config_bucket = "venus-0529"

        # Download the configuration files from S3
        s3_client.download_file(config_bucket, "yolo_tiny_configs/coco.names", label_path)
        s3_client.download_file(config_bucket, "yolo_tiny_configs/yolov3-tiny.weights", weight_path)
        s3_client.download_file(config_bucket, "yolo_tiny_configs/yolov3-tiny.cfg", cfg_path)

        Labels = get_labels(label_path)

        # Download the latest object
        image_path = "/tmp/" + object_key.split("/")[-1]

        # Download the file from S3
        s3_client.download_file(BUCKET_NAME, object_key, image_path)
        image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{object_key}"

        # Read the image file
        image = cv2.imread(image_path)
        retval, buffer = cv2.imencode('.jpg', image)
        image_bytes = buffer.tobytes()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
        image_data = base64.b64decode(image_base64)
        image_np = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Load model and do object detection
        nets = load_model(cfg_path, weight_path)
        objects_list = do_prediction(image, nets, Labels)
        store_tags(image_url, objects_list)

        return {
            "statusCode": 200,
            "body": json.dumps("Object detected and updated tags to database."),
        }


def store_tags(image_url, objects_list):
    table = dynamodb.Table(TABLE_NAME)

    table.update_item(
        Key={"id": image_url},
        UpdateExpression="SET Tags = :object_list",
        ExpressionAttributeValues={":object_list": objects_list},
        ReturnValues="UPDATED_NEW",
    )

    # Fetch users subscribed to the detected tags
    notify_users(image_url, objects_list)


def notify_users(image_url, objects_list):
    for obj in objects_list:
        tag = obj['label']
        # Publish a message to the tag-specific SNS topic
        topic_name = f"ImageTag_{tag}"
        topic_arn = sns_client.create_topic(Name=topic_name)['TopicArn']

        sns_client.publish(
            TopicArn=topic_arn,
            Message=json.dumps({
                "default": "Image with tags you subscribed to has been uploaded.",
                "email": f"An image with the following tags has been uploaded: {tag}\n{image_url}"
            }),
            MessageStructure='json',
            Subject='New Image Uploaded with Your Subscribed Tags'
        )


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
