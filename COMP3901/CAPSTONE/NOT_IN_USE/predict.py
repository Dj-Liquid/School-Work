#Checks if object is knife or gun
import os
import cv2
from ultralytics import YOLO

# Define the directory paths and model path
VIDEOS_DIR = os.path.join('.', 'videos') # Directory containing input videos
model_path = os.path.join('.', 'runs', 'detect', 'train24', 'weights', 'last.pt') # Path to YOLO model weights being used

# Initialize the video capture object for the default camera (0)
# video_path = os.path.join(VIDEOS_DIR, 'KnifeTest.mp4')

#cap = cv2.VideoCapture(video_path)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Read the first frame from the video to get its dimensions
ret, frame = cap.read()
H, W, _ = frame.shape  # Get the height and width of the frame

# Define the output video path and create a VideoWriter object for writing processed frames
video_path_out = '{}_out.mp4'.format(os.path.join(VIDEOS_DIR, 'VideoTest')) # Output video file path
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Loading the custom YOLO model
model = YOLO(model_path)

# Define the detection threshold
threshold = 0.25  # Minimum confidence score for detected objects to be considered

# Process each frame in the video
while ret:
    # Perform object detection on the current frame using the YOLO model
    results = model(frame)[0]
    
    # Iterate over each detected object in the frame
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result    # Extract bounding box coordinates, confidence score, and class ID

        # Check if the confidence score is above the threshold
        if score > threshold:
            # Draw a bounding box around the detected object
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            
            # Display the class label above the bounding box
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    
    # Display the processed frame with object detections
    cv2.imshow('Camera Feed', frame)

    # Write the processed frame to the output video
    out.write(frame)
    
    # Read the next frame from the video
    ret, frame = cap.read()
    
    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()


