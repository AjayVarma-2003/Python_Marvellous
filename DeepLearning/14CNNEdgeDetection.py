# Using CNN for edge detection / classification

# Real time image classification system using CNN

# This project is a real time image classification system using pre-trained Convolutional Neural Network
# (CNN) (MobileNetV2) and out webcam.
# Goal :- Capture live video from your webcam and classify each frame into one of the ImageNet
#         categories (like dog, cat, keyboard etc.)
# Core Idea :- Use a pre-trained CNN model (MobileNetV2) to recognize object without having to train from scratch.
# Output :- Display the webcam feed with a label (class name + confidence percentage) overlaid in real-time.



import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

def ImageClassifier():
        # Load pre-trained CNN
    model = MobileNetV2(weights = "imagenet")

    # Capture from webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # running loop
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error : Could not read frame.")
            break
        
        # Preprocess for MobileNetV2: BGR -> RGB, resize to 224 x 224, scale
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img, (224, 224))
        x = np.expand_dims(img_resized, axis = 0).astype(np.float32)
        x = preprocess_input(x)

        # Predictions
        preds = model.predict(x, verbose = 0)
        decoded = decode_predictions(preds, top = 1)[0][0]
        label = f"{decoded[1]} : {decoded[2] * 100:.1f} %"

        # Overlay prediction on the fame
        cv2.putText(frame, label, (16, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("CNN Classification", frame)

        # Exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

def main():
    ImageClassifier()

if __name__ == "__main__":
    main()