import cv2
import easyocr
import time
import os
from collections import Counter

# Initialize the cascade and EasyOCR reader once
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)
reader = easyocr.Reader(['en'])

cap = cv2.VideoCapture(0)

# Set width and height for the video capture
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0
last_ocr_time = 0
ocr_interval = 5  # Perform OCR every 5 seconds
ocr_results = []  # To store OCR results for averaging

# Ensure the output directory exists
output_dir = "plates"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_final_text(ocr_results):
    """
    Function to get the most common recognized text from the OCR results.
    It averages the results based on frequency of the recognized texts.
    """
    flat_results = [result[1] for result in ocr_results]  # Extract text from OCR results
    if flat_results:
        most_common_text = Counter(flat_results).most_common(1)[0][0]  # Get the most frequent text
        return most_common_text
    return None

while True:
    success, img = cap.read()  # Capture frame-by-frame

    if not success:
        print("Failed to capture image")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    # Detect plates
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            # Draw rectangle around the plate
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            # Extract ROI (Region of Interest)
            img_roi = img[y: y + h, x: x + w]
            cv2.imshow("ROI", img_roi)

            # Perform OCR every 5 seconds
            current_time = time.time()
            if current_time - last_ocr_time > ocr_interval:
                output = reader.readtext(img_roi)
                print("OCR Output:", output)

                # Add the current OCR output to the results list for averaging
                if output:
                    ocr_results.extend(output)

                # Display the most common text so far
                final_text = get_final_text(ocr_results)
                if final_text:
                    # Display the final averaged text on the main image
                    cv2.putText(img, final_text, (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                last_ocr_time = current_time  # Update the last OCR time

    # Show the result on the main image
    cv2.imshow("Result", img)

    # Save image when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        if 'img_roi' in locals():  # Check if img_roi exists (plate detected)
            cv2.imwrite(f"{output_dir}/scanned_img_{count}.jpg", img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1
        else:
            print("No plate detected to save.")

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

