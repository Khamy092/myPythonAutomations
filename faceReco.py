import cv2
import numpy as np

face_names = {
    "face_68.jpg": "Taqi",
}
# Load the cascade classifier
face_cascade = cv2.CascadeClassifier("facemodel.xml")

# Load the reference face
reference_face = cv2.imread("face_5.jpg", cv2.IMREAD_GRAYSCALE) # face_7.jpg is the reference face
# Read the input image
img = cv2.imread("image1.jpg")

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the input image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# save the faces into files 
# for (x, y, w, h) in faces:
#     face = gray[y:y + h, x:x + w]
#     cv2.imwrite("face_{}.jpg".format(np.random.randint(100)), face)

# Loop over the faces and compare each face with the reference face
for (x, y, w, h) in faces:
    face = gray[y:y + h, x:x + w]
    result = cv2.matchTemplate(face, reference_face, cv2.TM_CCOEFF_NORMED)
    _, max_value, _, max_location = cv2.minMaxLoc(result)
    if max_value > 0.9:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Add text to indicate that the face was found
        if "face_68.jpg" in face_names:
            cv2.putText(img, face_names["face_68.jpg"], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the output
cv2.imshow("Faces found", img)
cv2.waitKey()
