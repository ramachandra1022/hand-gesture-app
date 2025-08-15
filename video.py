import cv2
from gesture_detector import detect_gesture

gesture = ""
streaming = True  # flag to control video streaming

def generate_frames():
    global gesture, streaming
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while streaming:
        success, frame = cap.read()
        if not success:
            break
        frame = cv2.flip(frame, 1)
        gesture = detect_gesture(frame)

        cv2.putText(frame, gesture, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

def get_current_gesture():
    return gesture

def stop_streaming():
    global streaming
    streaming = False

def start_streaming():
    global streaming
    streaming = True

