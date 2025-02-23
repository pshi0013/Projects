# import the necessary packages
from flask import Flask, jsonify, request
import numpy as np
import sys
import time
import cv2
import os
import base64

app = Flask(__name__)

# construct the argument parse and parse the arguments
confthres = 0.3
nmsthres = 0.1

def get_labels(labels_path):
    # load the COCO class labels our YOLO model was trained on
    lpath=os.path.sep.join([yolo_path, labels_path])

    print(yolo_path)
    LABELS = open(lpath).read().strip().split("\n")
    return LABELS


def get_weights(weights_path):
    # derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.sep.join([yolo_path, weights_path])
    return weightsPath

def get_config(config_path):
    configPath = os.path.sep.join([yolo_path, config_path])
    return configPath

def load_model(configpath,weightspath):
    # load our YOLO object detector trained on COCO dataset (80 classes)
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configpath, weightspath)
    return net

def do_prediction(image,net,LABELS):

    (H, W) = image.shape[:2]
    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i - 1] for i in net.getUnconnectedOutLayers()]

    # construct a blob from the input image and then perform a forward
    # pass of the YOLO object detector, giving us our bounding boxes and
    # associated probabilities
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    #print(layerOutputs)
    end = time.time()

    # show timing information on YOLO
    print("[INFO] YOLO took {:.6f} seconds".format(end - start))

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    classIDs = []

    # loop over each of the layer outputs
    for output in layerOutputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            # print(scores)
            classID = np.argmax(scores)
            # print(classID)
            confidence = scores[classID]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > confthres:
                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])

                confidences.append(float(confidence))
                classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, confthres,
                            nmsthres)

    # TODO Prepare the output as required to the assignment specification
    result = []
    if len(idxs) > 0:
        # loop over the indexes we are keeping
        for i in idxs.flatten():
            item = {
                "label": LABELS[classIDs[i]],
                "accuracy": confidences[i],
                "rectangle": {
                    "left": boxes[i][0],
                    "top": boxes[i][1],
                    "width": boxes[i][2],
                    "height": boxes[i][3]
                }
            }
            result.append(item)
    return result

## argument
if len(sys.argv) != 3:
    raise ValueError("Argument list is wrong. Please use the following format:  {} {} {}".
                     format("python iWebLens_server.py", "<yolo_config_folder>", "<Image file path>"))

yolo_path = str(sys.argv[1])

## Yolov3-tiny versrion
labelsPath= "coco.names"
cfgpath= "yolov3-tiny.cfg"
wpath= "yolov3-tiny.weights"

Labels=get_labels(labelsPath)
CFG=get_config(cfgpath)
Weights=get_weights(wpath)
#nets = load_model(CFG, Weights)


#TODO, you should  make this console script into webservice using Flask
@app.route('/detect', methods=['POST'])
def main():
    try:
        data = request.get_json()

        image_data = data['image']

        image_bytes = base64.b64decode(image_data)

        nparr = np.frombuffer(image_bytes, np.uint8)

        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        nets = load_model(CFG, Weights)

        detections = do_prediction(img, nets, Labels)

        # Prepare the response
        response = {
            "id": data['id'],
            "objects": detections
        }

        return jsonify(response), 200

    except Exception as e:
         return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1070, debug=True)
