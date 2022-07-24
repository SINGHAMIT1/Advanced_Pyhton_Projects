import cv2

# loading pre-trained face detection model in directory
face_cascade = cv2.CascadeClassifier("face_detector.xml")

# choose an image on which I want to test my code
img = cv2.imread("HI.jpg")

# Detecting Faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)

# drawing rectangles around the detected faces
for x, y, w, h in faces:
    # Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 20)

# Syntax: cv2.imwrite(filename, image)

cv2.imwrite("face_detected.png", img)
print("successfully saved")
