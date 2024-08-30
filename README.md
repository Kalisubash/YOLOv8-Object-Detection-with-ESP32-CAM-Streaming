YOLOv8 Object Detection with ESP32-CAM Streaming
Overview
This project demonstrates real-time object detection using the YOLOv8 model with images streamed from an ESP32-CAM. The Python script captures images from an ESP32-CAM, detects objects such as cats and birds, and displays annotated results.

Features
Real-Time Object Detection: Uses YOLOv8 to detect and annotate objects.
ESP32-CAM Integration: Streams images from an ESP32-CAM over WiFi.
Resolution Options: Supports different image resolutions (low, medium, high) from the ESP32-CAM.

Requirements
Python Script
Python 3.x
opencv-python library
numpy library
ultralytics library (for YOLOv8)
Install the required libraries using pip:pip install opencv-python numpy ultralytics

ESP32-CAM Setup
ESP32-CAM module

see in the docs


Arduino IDE with ESP32 support
WiFi network credentials
Setup
ESP32-CAM Code
Install the Required Libraries:

Ensure you have the esp32cam and WebServer libraries installed in your Arduino IDE.

Upload the Code:
Open the Arduino IDE, paste the ESP32-CAM code into a new sketch, and upload it to your ESP32-CAM.

Connect to WiFi:
Replace WIFI_SSID and WIFI_PASS with your WiFi credentials in the ESP32-CAM code.

Obtain the IP Address:
After uploading, open the Serial Monitor to see the ESP32-CAM’s IP address.
Python Script
Configure the URL:
Replace url in the Python script with the IP address of your ESP32-CAM and the path to the image (e.g., 'http://<ESP32-IP>/cam-hi.jpg').
Run the Script:

Execute the Python script to start capturing and processing images from the ESP32-CAM.
View the Output:
The script will open a window displaying the image with detected objects. Press 'q' to quit the window.
Code Overview
Python Script
Model Initialization: Loads the YOLOv8 model for object detection.
Image Handling: Fetches images from the ESP32-CAM URL.
Object Detection: Processes images to detect and annotate objects (e.g., cats, birds).
Display: Shows the annotated images in a window.
ESP32-CAM Code
Camera Setup: Initializes the ESP32-CAM with different resolutions.
Web Server: Sets up a web server to stream JPEG images at different resolutions.
Endpoint Handlers: Handles requests to serve images at different resolutions.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to contribute to this project by opening issues or submitting pull requests for improvements or additional features.

This README covers the setup and usage of both the Python script and the ESP32-CAM server code, providing clear instructions for integration and operation.
