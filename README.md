<img width="1517" height="796" alt="birdimage" src="https://github.com/user-attachments/assets/262077f6-161d-4ffb-a5d4-c54de1625781" />#  AI-Powered Bird Detection & Automatic Water Sprinkler Prototype

An AI-based smart farming prototype that detects birds in real time using Computer Vision and automatically activates a water sprinkler to safely scare them away. The system ignores humans, ensuring safe operation.

---

##  Overview

Birds often cause damage to crops, fruits, and vegetables, leading to significant agricultural losses. Traditional bird deterrent methods are inefficient and require constant human intervention.

This prototype combines **Artificial Intelligence, Computer Vision, and Embedded Systems** to create an automated bird deterrent system.

The system uses a webcam for real-time monitoring. When a bird is detected, a servo motor rotates toward the target and a water pump sprays water to gently scare the bird away. If a human is detected, the system takes no action.

---

##  Features

-  Real-time Bird Detection
-  Human Detection
-  Automatic Water Spraying
-  Servo Motor Rotation
-  Arduino-Based Control
-  TensorFlow Lite Model
-  Computer Vision using OpenCV
-  Safe & Eco-Friendly Bird Deterrence

---

##  How It Works

1. Webcam captures live video.
2. Frames are processed using a TensorFlow Lite model.
3. AI classifies the object as:
   - Bird 
   - Human 
4. If a Bird is detected:
   - Python sends a command to Arduino.
   - Servo motor rotates.
   - Water pump turns ON.
   - Water is sprayed.
5. If a Human is detected:
   - No action is taken.

---

##  Tech Stack

### Software
- Python
- TensorFlow Lite
- OpenCV
- NumPy

### Hardware
- Arduino UNO
- USB Webcam
- SG90 Servo Motor
- Mini Water Pump
- L298N Motor Driver
- Jumper Wires

---

##  Project Structure

```
Bird-Detection-System/
│
├── model/
│   ├── model.tflite
│   └── labels.txt
│
├── Arduino/
│   └── bird_detection.ino
│
├── Python/
│   ├── main.py
│   
│
├── Images/
│
├── README.md
│
└── requirements.txt
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
```

### Run the Project

```bash
python main.py
```

---

##  Applications

-  Smart Agriculture
-  Orchard Protection
-  Vegetable Farms
-  Plant Nurseries
-  Home Gardens
-  Grain Storage Protection
-  Eco-Friendly Bird Deterrence
-  AI-Based Smart Farming

---

## Author

**Vikas**

B.Tech in Artificial Intelligence & Machine Learning

LinkedIn: [(https://in.linkedin.com/in/vikas-thakur-0a3a1b257)]

---

⭐ If you found this project interesting, don't forget to **Star** this repository!
