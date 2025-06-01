MCQ Paper Grader 📝

The MCQ Paper Grader is a web-based application that automates the grading of multiple-choice question (MCQ) answer sheets using image processing. Built with Streamlit for an intuitive interface, OpenCV for accurate bubble detection, and Pandas for result analysis, it enables educators to upload scanned images, detect filled bubbles, and compare responses against a JSON answer key. Results are displayed with interactive tables and progress bars, streamlining assessments and reducing manual effort. 🚀
✨ Features

📤 Image Upload: Supports JPG, PNG, and JPEG formats for scanned answer sheets.
🔍 Bubble Detection: Uses OpenCV’s contour analysis for high-accuracy bubble identification.
✅ Answer Comparison: Compares detected answers with a JSON key to compute scores.
📊 Result Visualization: Presents results in interactive tables and progress bars via Streamlit.
💻 Scalable & Cost-Effective: Runs on standard hardware with open-source tools, no specialized OMR scanners needed.

🛠️ Prerequisites

🐍 Python 3.8+
🌐 A modern web browser (e.g., Chrome, Firefox) for the Streamlit interface
📄 An answer key in JSON format (e.g., answer_key.json) with the structure:{
  "answers": {
    "Q1": "A",
    "Q2": "B",
    ...
  }
}



⚙️ Installation

Clone the Repository 📂:
git clone https://github.com/Jitenrai21/MCQsChecker
cd mcq-paper-grader


Create a Virtual Environment (optional but recommended) 🧪:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies 📦:
pip install -r requirements.txt

The requirements.txt should include:
streamlit==1.38.0
opencv-python==4.10.0.84
numpy==1.26.4
pandas==2.2.2


Prepare the Answer Key 🔑:

Place your answer_key.json file in the project root directory.
Ensure it follows the format shown in the Prerequisites section.



🚀 Usage

Run the Application ▶️:
streamlit run main.py

This launches the Streamlit server, accessible at http://localhost:8501.

Upload an Answer Sheet 📤:

Open the web interface in your browser.
Use the file uploader to select a scanned answer sheet image (JPG, PNG, or JPEG).
The system processes the image, detects filled bubbles, and compares answers with the answer key.


View Results 📊:

The processed image is displayed, followed by a result summary table showing question-wise correctness.
A progress bar visualizes the score, and the final score (e.g., 25/30) is highlighted with a success message.



📂 Project Structure
mcq-paper-grader/
├── main.py              # Main Streamlit application 🎨
├── utils.py             # Helper functions for image processing and analysis 🛠️
├── answer_key.json      # JSON file with correct answers 🔑
├── requirements.txt     # Project dependencies 📋
└── README.md            # This file 📖

📸 Example Answer Sheet
The system expects a standard answer sheet layout:

🗳️ Two columns, 15 questions each (30 questions total).
🔢 Four options per question (A, B, C, D).
✍️ Bubbles filled with a dark pen or marker.

For best results, ensure the scanned image is clear, with minimal distortion or shadows.
⚠️ Limitations

📏 Designed for a fixed layout (2 columns, 15 questions per column). Custom layouts require code modifications.
🖼️ Performance may vary with poor image quality (e.g., low resolution, smudges).
❓ Currently supports only MCQ formats, not open-ended questions.

🔮 Future Enhancements

🛠️ Support for customizable answer sheet layouts.
🌐 Integration with learning management systems (LMS) for result export.
🤖 Machine learning models to handle low-quality images or ambiguous marks.
📬 Real-time feedback for students via a student-facing interface.

🤝 Contributing
We welcome contributions! To get started:

🍴 Fork the repository.
🌿 Create a feature branch (git checkout -b feature/your-feature).
💾 Commit your changes (git commit -m "Add your feature").
🚀 Push to the branch (git push origin feature/your-feature).
📬 Open a pull request.

Please ensure your code follows PEP 8 guidelines and includes relevant tests.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙏 Acknowledgments

Built with Streamlit, OpenCV, and Pandas. 🎉
Inspired by the need for accessible, automated grading solutions in education. 🏫

📧 Contact
For questions or feedback, please contact me at [info@jitenrai.com.np] . ✉️
