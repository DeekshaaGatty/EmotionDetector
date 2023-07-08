# EmotionDetector
Real-time emotion detection using webcam feed and facial expression recognition with OpenCV and FER library.

## Working of the code:
1. The code imports necessary libraries: `cv2` for video processing, `matplotlib.pyplot` for image display, and `FER` for facial expression recognition.

2. It creates an instance of the `FER` class, enabling the MTCNN face detection model.

3. The code opens the webcam using `cv2.VideoCapture(0)`.

4. It starts an infinite loop to continuously process frames from the webcam.

5. Each frame is read using `webcam.read()` and stored in `ret` and `frame` variables.

6. The `detect_emotions()` method of the `FER` instance is used to detect emotions in the frame, and the result is stored in the `result` variable.

7. The code iterates over each detected face in the `result` list and extracts the bounding box coordinates and dominant emotion label.

8. It draws a rectangle around the detected face using `cv2.rectangle()` and displays the dominant emotion label using `cv2.putText()`.

9. The frame with the emotion detection overlay is shown using `cv2.imshow()`.

10. The code checks if the 'q' key is pressed to break the loop. If so, it releases the webcam using `webcam.release()` and closes all windows using `cv2.destroyAllWindows()`.

Overall, the code continuously captures frames from the webcam, detects faces, and identifies the dominant emotion for each face. It displays the frames with emotion detection overlays in real-time.
