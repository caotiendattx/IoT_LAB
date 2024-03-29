import cv2
import os

def get_image():
    # Use the first webcam device
    cap = cv2.VideoCapture(0)
    
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
    
    # Define the output directory to store the split images
    output_directory = "./assets/output_images"
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Placeholder for the split_image function
    # split_image(input_image_path, output_directory)
    
    # Release the webcam
    cap.release()

# Call the function to capture an image from the webcam
get_image()

# Print a success message
print("Webcam image captured and saved.")
