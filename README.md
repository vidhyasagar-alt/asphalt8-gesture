🚗 Asphalt 8 Hand Gesture Control
�

�
�
�
�
Load image
Load image
Load image
Load image
Control Asphalt 8 Airborne using just your hand gestures — no keyboard, no mouse, no controller!
🎓 Final Year Project | ECE Department | Podhigai College of Engineering and Technology
�

🎮 Demo
📹 Watch it in action: [Click here to watch demo](https://youtu.be/5eXwCaDdCNM?si=CnKYoj_cRAaMvYe7)
✨ What is this project?
This project uses your webcam and Artificial Intelligence to detect your hand gestures in real time and convert them into keyboard inputs to control Asphalt 8 Airborne on PC.
No physical controller needed — just your hand in front of the camera! 🖐️
🕹️ Gesture Controls
🖐️ Single Hand Control — Everything controlled with just ONE hand!
Gesture
Action
Key Mapped
✋ Move Hand Right
Steer Right
→ Arrow Key
✋ Move Hand Left
Steer Left
← Arrow Key
☝️ 1 Finger Up
Nitro Boost
N Key
✊ Close All Fingers
Brake
↓ Arrow Key
🚫 No Hand Detected
Pause / Resume
P Key
🧠 How It Works
Webcam captures video in real time
        ↓
MediaPipe detects 21 hand landmarks on single hand
        ↓
OpenCV checks hand position:
  ├── Hand moved RIGHT?     → Steer Right ➡️
  ├── Hand moved LEFT?      → Steer Left  ⬅️
  ├── 1 Finger raised?      → Nitro Boost ⚡
  ├── All fingers closed?   → Brake       🛑
  └── No hand detected?     → Pause/Resume ⏸️
        ↓
Python simulates the keyboard input
        ↓
🚗 Asphalt 8 responds instantly!
🛠️ Technologies Used
Technology
Purpose
Python
Core programming language
OpenCV
Real-time video capture and processing
MediaPipe
Hand landmark detection (21 points)
PyAutoGUI / Keyboard
Simulating keyboard inputs
⚙️ Installation & Setup
Prerequisites
Python 3.7 or above
Webcam
Asphalt 8 Airborne installed on PC
Windows OS
Step 1 — Clone the repository
git clone https://github.com/vidhyasagar-alt/asphalt8-gesture.git
cd asphalt8-gesture
Step 2 — Install required libraries
pip install -r requirements.txt
Step 3 — Run the project
python main.py
Step 4 — Play!
Open Asphalt 8 Airborne on your PC
Run the script
Place your single hand in front of the webcam
The game auto-detects and starts responding to gestures!
Remove hand from camera to pause, show hand again to resume
Start racing! 🏁
📦 Requirements
opencv-python
mediapipe
pyautogui
keyboard
numpy
📁 Project Structure
asphalt8-gesture/
│
├── main.py              # Main script — run this to start
├── requirements.txt     # All required libraries
└── README.md            # Project documentation
🎯 Key Features
✅ Real-time hand gesture detection
✅ Zero latency response to gestures
✅ 5 gesture controls — steer left/right, nitro, brake, pause/resume
✅ 21-point hand landmark detection using MediaPipe
✅ Works with any PC game that uses keyboard controls
✅ No external hardware needed — just a webcam!
🔮 Future Improvements
[ ] Add two-hand gesture support for more controls
[ ] Create a GUI to configure gestures
[ ] Support for more games
[ ] Add gesture sensitivity settings
[ ] Mobile phone camera support
👨‍💻 About the Developer
Vidhya Sagar
🎓 Final Year ECE Student
🏫 Podhigai College of Engineering and Technology
💡 Passionate about AI, Computer Vision and Embedded Systems
🔗 GitHub: @vidhyasagar-alt
📄 License
This project is licensed under the MIT License — feel free to use, modify and share!
�

⭐ If you found this project cool, please give it a star! ⭐
Made with ❤️ by Vidhya Sagar — ECE Department
Podhigai College of Engineering and Technology
�
