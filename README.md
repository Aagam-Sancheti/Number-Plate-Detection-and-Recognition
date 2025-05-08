# Number-Plate-Detection-and-Recognition using Haar Cascade and EasyOCR

This project is a Python-based Number Plate Recognition system that uses OpenCV’s Haar Cascade classifier to detect vehicles and extract number plates from a video or a live camera feed. The extracted number plate is then processed using EasyOCR to recognize and read the characters.
This was a team project which took lot of efforts and sleepless night but the final output is just amazing!

---

## 🚀 Features

- Capture images from:
  - Pre-recorded video
  - Live webcam feed
- Detect and extract number plates using Pre-trained Russian Haar Cascade model.
- Recognize characters using EasyOCR.
- Save and display results.

---

## 🛠 Technologies Used

- Python 3.12.2
- OpenCV (for image processing and number plate capture)
- EasyOCR (for Optical Character Recognition)

---

## 📁 Project Structure

<img width="943" alt="Screenshot 2025-05-06 at 1 35 22 PM" src="https://github.com/user-attachments/assets/34d488ac-f93c-4abd-80a4-36eb2d1d411b" />

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Aagam-Sancheti/Number-Plate-Detection-and-Recognition.git
cd Number-Plate-Detection-and-Recognition/FinalProject/
```

2. **Make a new Conda environment:**

```bash
conda create -n Number_plate_recognition
```

3. **Activate the environment:**

```bash
conda activate Number_plate_recognition
```

4. **Install dependencies from requirements.txt:**

```bash
pip install -r requirements.txt
```
5. **Run the video or webcam capture:**

```bash
python3 video_capture.py
# OR
python3 live_camera_capture.py
```

6. **Output will be visible on the terminal**
  <img width="1280" alt="Screenshot 2025-05-08 at 10 23 39 AM" src="https://github.com/user-attachments/assets/c6e1c091-2128-43e3-a659-84d94f137343" />
  ![image](https://github.com/user-attachments/assets/ea6be844-6aad-4d96-b92a-9aaae3f6f63f)

