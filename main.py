import streamlit as st
import cv2
import numpy as np
from utils import load_image, crop_answer_section, divide_into_zones, detect_answers, load_answer_key, compare_with_answer_key, display_results
import json
import tempfile
import os

st.title("📝 MCQ Paper Grader")

uploaded_file = st.file_uploader("Upload filled answer sheet image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_img_path = temp_file.name

    img = load_image(temp_img_path)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Uploaded Image", use_column_width=True)

    answer_section = crop_answer_section(img)
    zones = divide_into_zones(answer_section)
    answers = detect_answers(answer_section, zones)

    answer_key = load_answer_key()
    result_summary, correct = compare_with_answer_key(answers, answer_key)

    st.subheader("📊 Result Summary")
    # st.json(result_summary)
    display_results(result_summary)

    st.success(f"✅ Score: {correct}/{len(answers)}")

    # Optionally clean up temp file
    os.remove(temp_img_path)
