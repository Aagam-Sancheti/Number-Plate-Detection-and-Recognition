# Number-Plate-Detection-and-Recognition using Haar Cascade and EasyOCR

This project is a Python-based Number Plate Recognition system that uses OpenCV’s Haar Cascade classifier to detect vehicles and extract number plates from a video or a live camera feed. The extracted number plate is then processed using EasyOCR to recognize and read the characters.

---

 Features
	•	Capture images from:
		  Pre-recorded video (or)
	    Live webcam feed
	•	Detect and extract number plates using Pre-trained Russian Haar Cascade model.
	•	Recognize characters using EasyOCR.
	•	Save and display results

 ---
 
Technologies Used
	•	Python
	•	OpenCV (for image processing and Haar cascade detection)
	•	EasyOCR (for Optical Character Recognition)

---

Project Structure

├── FinalProject
│   ├── model
│   │   └── haarcascade_russian_plate_number.xml             # Haarcascade file for license plate detection
│   ├── NFT_project_liveCamera.py                            # Capture frames from a webcam (this can be connected to a live CCTV camera) 
│   ├── NFT_project.py                                       # Capture frames from a recorded video
│   ├── NFTfinaleval.pdf                                     # Presentation explaining the working
│   ├── output_frames                                        # save the intermediate frames for processing into OCR
│   ├── SampleVideo.mp4
│   ├── SampleVideo2.mp4
│   └── SampleVideo3.mp4
├── model
│   └── haarcascade_russian_plate_number.xml                
├── number_plate_2.py                                       # testing to fit in OCR model. Just incremental file to previous file.
├── number_plate.py                                         # initial model, just captures licence plates from live camera 
├── plates
│   ├── scaned_img_0.jpg                                    # intermediate folder to save frames
│   └── scanned_img_0.jpg
├── pptnft.pdf                                              # intermediate presentation before incorporating OCR 
└── requirements.txt                                        # download the requirement into your python environment

---

## ⚙️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Aagam-Sancheti/Number-Plate-Detection-and-Recognition.git
cd Number-Plate-Detection-and-Recognition
