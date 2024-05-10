import cv2
import os

def get_image():
    # Use the first webcam device
    cap = cv2.VideoCapture('rtsp://admin:admin@172.28.182.32:1935')
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Check if frame was successfully read
    if not ret:
        print("Error: Unable to capture frame.")
        return
    
    # Resize the frame to the desired resolution
    frame = cv2.resize(frame, (640, 480))
    
    # Define the path to save the captured frame
    input_image_path = "./assets/frame.jpg"
    
    # Save the captured frame to the defined path
    cv2.imwrite(input_image_path, frame)
    
    # Release the webcam
    cap.release()



def open_camera():
    while True:

        # Capture the video frame
        # by 
        vid = cv2.VideoCapture('rtsp://admin:admin@172.28.182.32:1935')
        ret, frame = vid.read()
        # Display the resulting frame
        cv2.imshow("frame", frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

open_camera()
