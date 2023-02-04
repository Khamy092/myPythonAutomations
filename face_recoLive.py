import cv2

# Load the cascades for face detection
face_cascade = cv2.CascadeClassifier("facemodel.xml")

# Load the video stream
video_capture = cv2.VideoCapture(0)

# Start the loop to process the video stream
while True:
    # Get the next frame from the video stream
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Loop through each face in the frame
    for (x, y, w, h) in faces:
        # Draw a box around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    # Display the results
    cv2.imshow("Video", frame)
    
    # Check if the user pressed the 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video stream and close the window
video_capture.release()
cv2.destroyAllWindows()
