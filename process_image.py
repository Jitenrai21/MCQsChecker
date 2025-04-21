import cv2 
# import pytesseract
import numpy as np
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import json

# To read image 
img = cv2.imread("images/mcqs_paper_Filled.jpg", cv2.IMREAD_COLOR) 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

height, width = img.shape[:2]

# Define margins manually (tune these values as needed)
top_margin = 120      # pixels to skip header
bottom_margin = 160   # pixels to skip footer
left = 0
right = width

# Crop answer section only
answer_section = img[top_margin:height - bottom_margin, left:right]
answer_height, answer_width = answer_section.shape[:2]

# Grid dimensions
questions_per_col = 15
col_width = answer_width // 2
row_height = answer_height // questions_per_col

zones = []

for col in range(2):  # Left and right column
    for row in range(questions_per_col):
        x = col * col_width
        y = row * row_height
        w = col_width
        h = row_height

        zones.append((x, y, w, h))

        # Draw rectangle on answer_section (not the original img)
        cv2.rectangle(answer_section, (x, y), (x + w, y + h), (0, 0, 255), 1) #(image, start_point, end_point, color, thickness)

answers = []

for i, (x, y, w, h) in enumerate(zones):
    question_img = answer_section[y:y+h, x:x+w]
    question_gray = cv2.cvtColor(question_img, cv2.COLOR_BGR2GRAY)
    
    # Adaptive threshold for better handling of lighting
    thresh = cv2.adaptiveThreshold(question_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY_INV, 11, 2)

    # Detect contours in the question zone
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bubble_info = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 500 < area < 2000:
            x_b, y_b, w_b, h_b = cv2.boundingRect(cnt)
            bubble_img = question_gray[y_b:y_b+h_b, x_b:x_b+w_b]

            # Count number of black pixels inside the bubble
            mask = cv2.drawContours(np.zeros_like(thresh), [cnt], -1, 255, -1)
            filled_pixels = cv2.countNonZero(cv2.bitwise_and(thresh, thresh, mask=mask))
            filled_ratio = filled_pixels / area

            # If filled ratio is higher than threshold, it's marked
            marked = filled_ratio > 0.4  # You can tune this threshold
            bubble_info.append((x_b, y_b, filled_ratio, cnt))


    # Sort bubbles by x-position (assuming left to right is A, B, C, D)
    bubble_info.sort(key=lambda b: b[0])  # x_b position

    # Threshold to decide if marked
    marked_threshold = 0.4
    marked_bubbles = [(i, b) for i, b in enumerate(bubble_info) if b[2] > marked_threshold]

    if len(marked_bubbles) == 1:
        selected_option = chr(65 + marked_bubbles[0][0])
    elif len(marked_bubbles) > 1:
        # If multiple marked, pick the one with highest fill ratio
        best = max(marked_bubbles, key=lambda b: b[1][2])
        selected_option = chr(65 + best[0])
    else:
        selected_option = "Unmarked"

    answers.append(selected_option)

    # Draw all detected bubbles in green
    for bx, by, _, cnt in bubble_info:
        cv2.rectangle(answer_section, (x + bx, y + by), (x + bx + w_b, y + by + h_b), (0, 255, 0), 1)

    # Write selected option A/B/C/D
    cv2.putText(answer_section, f"Q{i+1}: {selected_option}", (x + 10, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)

# cv2.imshow("Contours on Answer Section", answer_section)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Load the answer key from JSON file
with open("answer_key.json", "r") as f:
    answer_key = json.load(f)["answers"]

# Compare and generate result
correct = 0
result_summary = {}

for idx, student_answer in enumerate(answers):
    q_key = f"Q{idx + 1}"
    correct_answer = answer_key.get(q_key, "N/A")
    is_correct = student_answer == correct_answer
    result_summary[q_key] = {
        "StudentAnswer": student_answer,
        "CorrectAnswer": correct_answer,
        "IsCorrect": is_correct
    }
    if is_correct:
        correct += 1

# Print results
# print(json.dumps(result_summary, indent=4))
# print(f"\nTotal Correct: {correct}/{len(answers)}")