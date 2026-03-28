<div align="center">

# 🚗 Asphalt 8 — Hand Gesture Control

### Control Asphalt 8 Airborne with just your hand — no keyboard, no mouse, no controller!

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Detection-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black?style=for-the-badge&logo=github)](https://github.com/vidhyasagar-alt/asphalt8-gesture)

<br/>

> 🎓 **Final Year Project** &nbsp;|&nbsp; ECE Department &nbsp;|&nbsp; Podhigai College of Engineering and Technology

</div>

---

## 🎬 Demo

> 📹 **Watch it in action:** [▶️ Click here to watch demo](https://youtu.be/5eXwCaDdCNM?si=CnKYoj_cRAaMvYe7)

---

## ✨ What is this project?

This project uses your **webcam** and **Artificial Intelligence** to detect your hand gestures in real time and convert them into keyboard inputs to control **Asphalt 8 Airborne** on PC.

> 🖐️ **No physical controller needed — just your hand in front of the camera!**

---

## 🕹️ Gesture Controls

> 🖐️ **Single Hand Control — Everything controlled with just ONE hand!**

| Gesture | Action | Key Mapped |
|---------|--------|------------|
| ✋ Move Hand Right | Steer Right | `→` Arrow Key |
| ✋ Move Hand Left | Steer Left | `←` Arrow Key |
| ☝️ 1 Finger Up | Nitro Boost ⚡ | `N` Key |
| ✊ Close All Fingers | Brake 🛑 | `↓` Arrow Key |
| 🚫 No Hand Detected | Pause / Resume | `P` Key |

---

## 🧠 How It Works

```
📷 Webcam captures video in real time
        ↓
🖐️ MediaPipe detects 21 hand landmarks on single hand
        ↓
👁️ OpenCV checks hand position:
  ├── Hand moved RIGHT?     → Steer Right  ➡️
  ├── Hand moved LEFT?      → Steer Left   ⬅️
  ├── 1 Finger raised?      → Nitro Boost  ⚡
  ├── All fingers closed?   → Brake        🛑
  └── No hand detected?     → Pause/Resume ⏸️
        ↓
⌨️ Python simulates the keyboard input
        ↓
🚗 Asphalt 8 responds instantly!
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core programming language |
| 👁️ OpenCV | Real-time video capture and processing |
| 🖐️ MediaPipe | Hand landmark detection (21 points) |
| ⌨️ PyAutoGUI / Keyboard | Simulating keyboard inputs |

---

## ⚙️ Installation & Setup

### ✅ Prerequisites
- Python 3.7 or above
- Webcam
- Asphalt 8 Airborne installed on PC
- Windows OS

### 📥 Step 1 — Clone the Repository
```bash
git clone https://github.com/vidhyasagar-alt/asphalt8-gesture.git
cd asphalt8-gesture
```

### 📦 Step 2 — Install Required Libraries
```bash
pip install -r requirements.txt
```

### ▶️ Step 3 — Run the Project
```bash
python main.py
```

### 🎮 Step 4 — Play!
1. Open **Asphalt 8 Airborne** on your PC
2. Run the script
3. Place your **single hand** in front of the webcam
4. The game auto-detects and starts responding to gestures!
5. Remove hand from camera to **pause**, show hand again to **resume**
6. 🏁 Start racing!

---

## 📦 Requirements

```
opencv-python
mediapipe
pyautogui
keyboard
numpy
```

---

## 📁 Project Structure

```
asphalt8-gesture/
│
├── main.py              # 🚀 Main script — run this to start
├── requirements.txt     # 📦 All required libraries
└── README.md            # 📄 Project documentation
```

---

## 🎯 Key Features

| Feature | Status |
|---------|--------|
| ⚡ Real-time hand gesture detection | ✅ |
| 🏎️ Zero latency response to gestures | ✅ |
| 🕹️ 5 gesture controls (steer, nitro, brake, pause/resume) | ✅ |
| 🖐️ 21-point hand landmark detection via MediaPipe | ✅ |
| 🎮 Works with any PC game using keyboard controls | ✅ |
| 📷 No external hardware — just a webcam! | ✅ |

---

## 🔮 Future Improvements

- [ ] 🤲 Add two-hand gesture support for more controls
- [ ] 🖥️ Create a GUI to configure gestures
- [ ] 🎮 Support for more games
- [ ] 🎚️ Add gesture sensitivity settings
- [ ] 📱 Mobile phone camera support

---

## 👨‍💻 About the Developer

<div align="center">

**Vidhya Sagar**

🎓 Final Year ECE Student &nbsp;|&nbsp; 🏫 Podhigai College of Engineering and Technology

💡 Passionate about AI, Computer Vision and Embedded Systems

[![GitHub](https://img.shields.io/badge/GitHub-vidhyasagar--alt-black?style=for-the-badge&logo=github)](https://github.com/vidhyasagar-alt)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/vidhya-sagar-4bba5339b)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail)](mailto:vidhyasagarboomi@gmail.com)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify and share!

---

<div align="center">

⭐ **If you found this project cool, please give it a star!** ⭐

Made with ❤️ by **Vidhya Sagar** — ECE Department, Podhigai College of Engineering and Technology

🔗 **[View on GitHub](https://github.com/vidhyasagar-alt/asphalt8-gesture)**

</div>
