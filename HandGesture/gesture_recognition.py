import cv2
import mediapipe as mp
import pyttsx3

# Initialize Mediapipe and TTS engine
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
engine = pyttsx3.init()

# Define gesture mappings
GESTURE_TEXT = {
    "thumbs_up": "Hello",
    "fist": "Yes",
    "palm": "No"
}

def recognize_gesture(landmarks):
    """Basic gesture recognition logic"""
    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    pinky_tip = landmarks[20].y
    palm_base = landmarks[0].y

    if thumb_tip < palm_base and index_tip > palm_base:
        return "thumbs_up"
    elif all(landmarks[i].y > palm_base for i in range(1, 21)):
        return "fist"
    elif all(landmarks[i].y < palm_base for i in range(1, 21)):
        return "palm"
    return None

# Start Video Capture
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert color and process frame
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Recognize gesture
                gesture = recognize_gesture(landmarks.landmark)
                if gesture and gesture in GESTURE_TEXT:
                    text = GESTURE_TEXT[gesture]
                    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    # Convert text to speech
                    engine.say(text)
                    engine.runAndWait()

        cv2.imshow("Hand Gesture Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
