FROM python:3.11-slim-bullseye
WORKDIR /a1
ENV FLASK_APP object_detection.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    libgl1-mesa-dev \
    libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY object_detection.py .
COPY yolo_tiny_configs/ .

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 1070
CMD ["sh", "-c", "python object_detection.py yolo_tiny_configs/ image.jpg"]