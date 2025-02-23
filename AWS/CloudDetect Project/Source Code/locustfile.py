from locust import HttpUser, task, between
import os
import base64
import json
import uuid
import time

class ImageUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://152.69.181.138:30023"  # Specify the base host here

    @task
    def load_image(self):
        image_dir = '/Users/peichunshih/FIT5225Assi1/inputfolder'
        images = os.listdir(image_dir)

        for image_name in images:
            with open(os.path.join(image_dir, image_name), 'rb') as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

            data = {
                "id": str(uuid.uuid4()),
                "image": image_base64
            }
            headers = {'Content-Type': 'application/json'}

            try:
                response = self.client.post("/detect", data=json.dumps(data), headers=headers)
                print(response.text)
                if response.status_code != 200:
                    print(f"Error: Received status code {response.status_code} for image {image_name}")
            except Exception as e:
                print(f"Error occurred while processing image {image_name}: {e}")

            time.sleep(1)
