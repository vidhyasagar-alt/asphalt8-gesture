import cv2
import mediapipe as mp
import pyautogui
import time
import keyboard
pyautogui.PAUSE = 0  
pyautogui.FAILSAFE = False 
MODEL_PATH = r"D:\PY project\hand_landmarker.task"

frame_count = 0
last_result = None 

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1 
)

try:
    landmarker = HandLandmarker.create_from_options(options)
except Exception as e:
    print(f"❌ Error: {e}")
    exit()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

keys = {"up": False, "down": False, "left": False, "right": False}

def control(key_to_press):
    if key_to_press and not keys[key_to_press]:
        pyautogui.keyDown(key_to_press)
        keys[key_to_press] = True

def release(key_to_release):
    if keys[key_to_release]:
        pyautogui.keyUp(key_to_release)
        keys[key_to_release] = False

def release_all():
    for k in keys:
        if keys[k]:
            pyautogui.keyUp(k)
            keys[k] = False

print("🏎️ Steer Mode Optimized. Single Finger = Nitro. 'Q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    ts = int(time.time() * 1000) 
    last_result = landmarker.detect_for_video(mp_image, ts)

    status = "STRAIGHT"

    if last_result and last_result.hand_landmarks:
        landmarks = last_result.hand_landmarks[0]
        
        hand_x = landmarks[5].x 
        
        index_tip = landmarks[8]
        index_pip = landmarks[6]
        middle_tip = landmarks[12]
        middle_pip = landmarks[10]

        if hand_x < 0.43:
            control("left")
            release("right")
            status = "STEER LEFT"
        elif hand_x > 0.57:
            control("right")
            release("left")
            status = "STEER RIGHT"
        else:
            release("left")
            release("right")
            status = "STRAIGHT"
        index_up = index_tip.y < index_pip.y
        middle_up = middle_tip.y < middle_pip.y
        if index_up and not middle_up:
            pyautogui.press("space")
            control("up")
            release("down")
            status += " + NITRO"
            
        elif not index_up:
            control("down")
            release("up")
            status += " + BRAKE"
        else:
            control("up")
            release("down")
            status += " + GAS"
    else:
        release_all()
        status = "HAND LOST"
    cv2.line(frame, (int(w*0.43), 0), (int(w*0.43), h), (0, 255, 255), 1)
    cv2.line(frame, (int(w*0.57), 0), (int(w*0.57), h), (0, 255, 255), 1)
    
    cv2.putText(frame, status, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("High-Speed Steer Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or keyboard.is_pressed('q'):
        break

release_all()
cap.release()
cv2.destroyAllWindows()