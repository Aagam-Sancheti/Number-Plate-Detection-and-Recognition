# Number-Plate-Detection-and-Recognition using Haar Cascade and EasyOCR

This project is a Python-based Number Plate Recognition system that uses OpenCV’s Haar Cascade classifier to detect vehicles and extract number plates from a video or a live camera feed. The extracted number plate is then processed using EasyOCR to recognize and read the characters.

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

- Python
- OpenCV (for image processing and Haar cascade detection)
- EasyOCR (for Optical Character Recognition)

---

## 📁 Project Structure

FinalProject/
├── model/
│   └── haarcascade_russian_plate_number.xml      # Haarcascade file for license plate detection
├── NFT_project_liveCamera.py                     # Capture frames from a webcam (can be connected to a live CCTV feed)
├── NFT_project.py                                # Capture frames from a recorded video
├── NFTfinaleval.pdf                              # Final presentation explaining the working
├── output_frames/                                # Intermediate frames saved for OCR processing
├── SampleVideo.mp4                               # Sample input video 1
├── SampleVideo2.mp4                              # Sample input video 2
├── SampleVideo3.mp4                              # Sample input video 3

model/
└── haarcascade_russian_plate_number.xml          # Duplicate cascade model (if used outside FinalProject)

number_plate_2.py                                  # Testing script with OCR integration (incremental update)
number_plate.py                                    # Initial model for capturing license plates from live camera

plates/
├── scaned_img_0.jpg                              # Saved frame for testing
└── scanned_img_0.jpg                             # Another saved frame (possible duplicate or test)

pptnft.pdf                                         # Intermediate presentation before OCR integration

requirements.txt                                   # Python dependencies

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Aagam-Sancheti/Number-Plate-Detection-and-Recognition.git
cd Number-Plate-Detection-and-Recognition
