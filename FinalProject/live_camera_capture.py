import cv2
import easyocr
import imutils

# Function to sort contours
def sort_cont(character_contours):
    """
    To sort contours
    """
    i = 0
    boundingBoxes = [cv2.boundingRect(c) for c in character_contours]

    (character_contours, boundingBoxes) = zip(*sorted(zip(character_contours, boundingBoxes),
                                                    key=lambda b: b[1][i],
                                                    reverse=False))

    return character_contours

# Function to segment characters on the plate
def segment_chars(plate_img, fixed_width):
    """
    Extract Value channel from the HSV format
    of image and apply adaptive thresholding
    to reveal the characters on the license plate
    """
    V = cv2.split(cv2.cvtColor(plate_img, cv2.COLOR_BGR2HSV))[2]

    thresh = cv2.adaptiveThreshold(V, 255,
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY,
                                  11, 2)

    thresh = cv2.bitwise_not(thresh)

    plate_img = imutils.resize(plate_img, width=fixed_width)
    thresh = imutils.resize(thresh, width=fixed_width)
    bgr_thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

    # This part segments the characters on the plate
    labels = measure.label(thresh, background=0)
    charCandidates = np.zeros(thresh.shape, dtype='uint8')

    characters = []
    for label in np.unique(labels):
        if label == 0:
            continue

        labelMask = np.zeros(thresh.shape, dtype='uint8')
        labelMask[labels == label] = 255

        cnts = cv2.findContours(labelMask,
                    cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)

        cnts = cnts[1] if imutils.is_cv3() else cnts[0]

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            (boxX, boxY, boxW, boxH) = cv2.boundingRect(c)

            aspectRatio = boxW / float(boxH)
            solidity = cv2.contourArea(c) / float(boxW * boxH)
            heightRatio = boxH / float(plate_img.shape[0])

            keepAspectRatio = aspectRatio < 1.0
            keepSolidity = solidity > 0.15
            keepHeight = heightRatio > 0.5 and heightRatio < 0.95

            if keepAspectRatio and keepSolidity and keepHeight and boxW > 14:
                hull = cv2.convexHull(c)
                cv2.drawContours(charCandidates, [hull], -1, 255, -1)

    contours, hier = cv2.findContours(charCandidates,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        contours = sort_cont(contours)
        addPixel = 4
        for c in contours:
            (x, y, w, h) = cv2.boundingRect(c)
            if y > addPixel:
                y = y - addPixel
            else:
                y = 0
            if x > addPixel:
                x = x - addPixel
            else:
                x = 0
            temp = bgr_thresh[y:y + h + (addPixel * 2),
                            x:x + w + (addPixel * 2)]

            characters.append(temp)

        return characters

    else:
        return None

# Main function for camera processing
def process_camera(output_dir):
    reader = easyocr.Reader(['en'])
    print("Processing camera...")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Load the pre-trained Haar Cascade model for plate detection
    plate_cascade = cv2.CascadeClassifier('model/haarcascade_russian_plate_number.xml')

    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        if frame_count % 30 == 0:
            print(f"Processing frame {frame_count}...")

            # Convert to grayscale for Haar Cascade detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect plates using Haar Cascade
            plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

            if len(plates) > 0:
                for (x, y, w, h) in plates:
                    plate_img = frame[y:y + h, x:x + w]
                    result = reader.readtext(plate_img)

                    # Read and display the OCR result
                    for detection in result:
                        print(f"Detected text: {detection[1]}")

                    # Draw rectangle around the detected plate for visualization
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        frame_count += 1

        # Display the processed frame
        cv2.imshow('Processed Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Processing complete!")

# Example usage
process_camera('output_frames')