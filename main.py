import cv2
import numpy as np
import tensorflow as tf
import serial
import time

# ==========================
# Arduino Serial Port
# ==========================
arduino = serial.Serial('COM11', 9600)   # Change COM3 if needed
time.sleep(2)

# ==========================
# Load TFLite Model
# ==========================
interpreter = tf.lite.Interpreter(model_path="model_unquant.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Get model input size automatically
height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

print("Input Size :", width, "x", height)

# ==========================
# Labels
# ==========================
labels = ["bird", "human"]

# ==========================
# Webcam
# ==========================
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

last_sent = ""

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Flip image
    frame = cv2.flip(frame,1)

    # Resize for model
    image = cv2.resize(frame,(width,height))

    # Normalize
    input_data = np.expand_dims(image.astype(np.float32)/255.0, axis=0)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]['index'])[0]

    index = np.argmax(prediction)

    confidence = prediction[index]

    label = labels[index]

    text = f"{label} : {confidence*100:.2f}%"

    cv2.putText(frame,text,(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,(0,255,0),2)

    # ==========================
    # Bird Detection
    # ==========================
    if label=="bird" and confidence>0.90:

        if last_sent!="B":
            arduino.write(b'B')
            print("Bird Detected")
            last_sent="B"

    # ==========================
    # Human Detection
    # ==========================
    elif label=="human" and confidence>0.90:

        if last_sent!="H":
            arduino.write(b'H')
            print("Human Detected")
            last_sent="H"

    cv2.imshow("Bird Detection",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()