import cv2
import numpy as np
import urllib.request
from ultralytics import YOLO

# Load the YOLOv8 model (you can use 'yolov8n.pt' or another YOLOv8 model)
model = YOLO("yolov8n.pt")

# URL of the video stream or image source
url = 'http://192.168.1.96/cam-hi.jpg'

# Function to detect and annotate objects
def find_objects(img):
    # Run the YOLOv8 model on the image
    results = model(img)

    found_cat = False
    found_bird = False

    # Iterate over the results
    for result in results:
        for box in result.boxes:
            # Get the class name and confidence of the detected object
            class_name = model.names[int(box.cls)]
            confidence = box.conf

            # Check if the object is a cat or a bird
            if class_name == 'bird':
                found_bird = True
            elif class_name == 'cat':
                found_cat = True

            # Get the bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Draw the bounding box and label on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.putText(img, f'{class_name.upper()} {int(confidence * 100)}%', 
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    return img, found_cat, found_bird

# Main loop to process the video stream
while True:
    # Get the image from the URL
    img_resp = urllib.request.urlopen(url)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgnp, -1)

    # Detect objects in the image
    img, found_cat, found_bird = find_objects(img)

    # Display the image with detected objects
    cv2.imshow('Image', img)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
