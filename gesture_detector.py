import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Simple gesture recognition (e.g., fingers up = count)
def detect_gesture(frame):
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
    gesture_text = ""

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            landmarks = hand_landmarks.landmark
            fingers = []

            # Check handedness
            label = handedness.classification[0].label  # "Left" or "Right"

            # Thumb
            if label == "Right":
                if landmarks[4].x < landmarks[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:  # Left hand
                if landmarks[4].x > landmarks[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Other 4 fingers
            for tip in [8, 12, 16, 20]:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            count = sum(fingers)
            gesture_text = f"Fingers: {count}"

    hands.close()
    return gesture_text
