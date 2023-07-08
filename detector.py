import cv2
import matplotlib.pyplot as plt
from fer import FER

# Build the Face detector
face_detector = FER(mtcnn=True)

# Open the webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    ret, frame = webcam.read()

    # Detect emotions in the frame
    result = face_detector.detect_emotions(frame)

    # Display the frame with the dominant emotion label
    for face in result:
        x, y, w, h = face['box']
        emotions = face['emotions']
        dominant_emotion = max(emotions, key=emotions.get)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Emotion Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
webcam.release()
cv2.destroyAllWindows()
