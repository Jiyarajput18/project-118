import cv2


# Create our body classifier
body_classifier = cv2.cascadeClassifier("haarcascade_fullboy.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(grey,1.2,3)
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
