import cv2
import easyocr
import os
import time

def process_video_with_haar(input_video_path, output_dir, haar_cascade_path):
    """
    Processes a video to detect license plates using a Haar Cascade model.
    Args:
        input_video_path: Path to the input video file.
        output_dir: Directory where processed frames will be saved.
        haar_cascade_path: Path to the Haar Cascade XML file for license plate detection.
    """
    # Load the Haar Cascade model
    plate_cascade = cv2.CascadeClassifier(haar_cascade_path)
    reader = easyocr.Reader(['en'])  # Initialize EasyOCR reader
    print("Processing video...")

    # Open the video file
    cap = cv2.VideoCapture(input_video_path)
    frame_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total frame count for progress tracking

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process every 30th frame for efficiency
        if frame_count % 30 == 0:
            print(f"Processing frame {frame_count}/{total_frames}...")

            # Convert frame to grayscale for Haar Cascade detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect plates using Haar Cascade
            plates = plate_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(plates) > 0:
                for (x, y, w, h) in plates:
                    # Crop the plate region
                    plate_img = frame[y:y + h, x:x + w]

                    # Perform OCR on the plate using EasyOCR
                    result = reader.readtext(plate_img)

                    # Display and log the OCR results
                    for detection in result:
                        print(f"Detected text: {detection[1]}")
                        # Draw a rectangle around the detected plate
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the processed frame
            cv2.imshow('Processed Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  # Allow early exit by pressing 'q'

            # Save the processed frame to the output directory
            frame_filename = os.path.join(output_dir, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved frame {frame_count} to {frame_filename}")

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    print("Processing complete!")
    print(f"Total frames processed: {frame_count}")

# Example usage
haar_cascade_path = 'model/haarcascade_russian_plate_number.xml'  # Update with the path to your Haar Cascade file
process_video_with_haar('SampleVideo2.mp4', 'output_frames', haar_cascade_path)