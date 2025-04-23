import cv2
import numpy as np
import json
import streamlit as st
import pandas as pd

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def crop_answer_section(img, top_margin=120, bottom_margin=160):
    height, width = img.shape[:2]
    return img[top_margin:height - bottom_margin, 0:width]

def divide_into_zones(answer_section, questions_per_col=15):
    zones = []
    answer_height, answer_width = answer_section.shape[:2]
    col_width = answer_width // 2
    row_height = answer_height // questions_per_col

    for col in range(2):
        for row in range(questions_per_col):
            x = col * col_width
            y = row * row_height
            zones.append((x, y, col_width, row_height))
    return zones

def detect_answers(answer_section, zones):
    answers = []
    for i, (x, y, w, h) in enumerate(zones):
        question_img = answer_section[y:y+h, x:x+w]
        question_gray = cv2.cvtColor(question_img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(question_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        bubble_info = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if 500 < area < 2000:
                x_b, y_b, w_b, h_b = cv2.boundingRect(cnt)
                mask = np.zeros_like(thresh)
                cv2.drawContours(mask, [cnt], -1, 255, -1)
                filled_pixels = cv2.countNonZero(cv2.bitwise_and(thresh, thresh, mask=mask))
                filled_ratio = filled_pixels / area
                bubble_info.append((x_b, y_b, filled_ratio, cnt))

        bubble_info.sort(key=lambda b: b[0])
        # Count how many bubbles are considered marked
        marked_indices = [i for i, b in enumerate(bubble_info) if b[2] > 0.4]

        if len(marked_indices) == 1:
            selected_option = chr(65 + marked_indices[0])  # A/B/C/D
        elif len(marked_indices) > 1:
            selected_option = "Multiple Selected"
        else:
            selected_option = "Unmarked"

        answers.append(selected_option)
    return answers


def load_answer_key(json_path="answer_key.json"):
    with open(json_path, "r") as f:
        return json.load(f)["answers"]

def compare_with_answer_key(student_answers, answer_key):
    result_summary = {}
    correct = 0

    for idx, student_answer in enumerate(student_answers):
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
    return result_summary, correct

def display_results(result_summary):
    st.subheader("📋 Result Summary")

    # Convert to DataFrame
    df = pd.DataFrame.from_dict(result_summary, orient='index')
    df.index.name = "Question"
    df.reset_index(inplace=True)

    # Add a nicer label for correct answers
    df['IsCorrect'] = df['IsCorrect'].apply(lambda x: "✅ Correct" if x else "❌ Wrong")

    # Show results in a table
    st.dataframe(df, use_container_width=True)

    # Count correct answers
    total_questions = len(df)
    total_correct = df['IsCorrect'].str.contains("✅").sum()

    st.markdown("---")
    st.success(f"🎯 Score: **{total_correct} / {total_questions}**")
    st.progress(total_correct / total_questions)