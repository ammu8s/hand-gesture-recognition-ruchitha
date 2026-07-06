# ✋ Hand Gesture Recognition using CNN and MediaPipe

A real-time Hand Gesture Recognition system that detects and classifies hand gestures using **Convolutional Neural Networks (CNN)** and **MediaPipe**. The project recognizes predefined hand gestures from images, videos, and live webcam feeds and converts selected gestures into text and speech.

---

## 📌 Features

- 🎥 Real-time hand gesture recognition using webcam
- 🖼️ Gesture recognition from images
- 📹 Gesture recognition from recorded videos
- 🧠 CNN-based gesture classification
- ✋ Hand landmark detection using MediaPipe
- 🔊 Text-to-Speech output using pyttsx3
- 🖥️ Simple GUI built with Tkinter

---

## 🛠️ Technologies Used

- Python
- OpenCV
- TensorFlow / Keras
- MediaPipe
- NumPy
- Tkinter
- pyttsx3
- Pickle

---

## 📂 Project Structure

```
HandGestureRecognition/
│
├── HandGestureRecognize.py      # GUI application
├── gesture_recognition.py       # MediaPipe real-time recognition
├── test.py                      # CNN model training/testing
├── model/
│   ├── model.json
│   ├── model_weights.h5
│   ├── X.txt.npy
│   ├── Y.txt.npy
│   └── history.pckl
├── Dataset/
├── testImages/
├── video/
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/HandGestureRecognition.git
```

Move into the project folder

```bash
cd HandGestureRecognition
```

Install dependencies

```bash
pip install opencv-python mediapipe tensorflow keras numpy pyttsx3 pillow
```

---

## ▶️ Running the Project

### GUI Version

```bash
python HandGestureRecognize.py
```

This application allows you to:

- Upload Dataset
- Train CNN Model
- Test Gesture Images
- Recognize Gestures from Videos

---

### MediaPipe Real-Time Recognition

```bash
python gesture_recognition.py
```

Recognized gestures are:

- 👍 Thumbs Up → Hello
- ✊ Fist → Yes
- ✋ Palm → No

The application also converts the recognized gesture into speech.

---

## 🧠 CNN Model

The CNN model is trained to classify multiple hand gestures.

Example gesture classes include:

- Palm
- I
- Fist
- Fist Moved
- Thumb
- Index
- OK
- Palm Moved
- C
- Down

---

## 📊 Workflow

```
Input Image / Webcam / Video
            │
            ▼
Image Preprocessing
            │
            ▼
Hand Detection
            │
            ▼
CNN Classification
            │
            ▼
Gesture Prediction
            │
            ▼
Display Result + Text-to-Speech
```

---

## 📸 Future Improvements

- Support Indian Sign Language (ISL)
- Add more gesture classes
- Improve model accuracy using transfer learning
- Deploy as a web application
- Mobile application support
- Sentence formation from continuous gestures

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository, create a feature branch, commit your changes, and submit a Pull Request.

---

## 📜 License

This project is intended for educational and research purposes.

---

## 👩‍💻 Author

**Ruchitha Ch**

If you found this project useful, consider giving it a ⭐ on GitHub!
