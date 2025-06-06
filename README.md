# 📝 MCQ Paper Grader

The **MCQ Paper Grader** is a web-based application that automates the grading of multiple-choice question (MCQ) answer sheets using image processing.

Built with **Streamlit** for an intuitive interface, **OpenCV** for accurate bubble detection, and **Pandas** for result analysis, it enables educators to:

- Upload scanned images
- Detect filled bubbles
- Compare responses against a JSON answer key

Results are displayed with interactive tables and progress bars, streamlining assessments and reducing manual effort. 🚀

---

## ✨ Features

- 📤 **Image Upload**: Supports JPG, PNG, and JPEG formats for scanned answer sheets  
- 🔍 **Bubble Detection**: Uses OpenCV’s contour analysis for high-accuracy bubble identification  
- ✅ **Answer Comparison**: Compares detected answers with a JSON key to compute scores  
- 📊 **Result Visualization**: Presents results in interactive tables and progress bars via Streamlit  
- 💻 **Scalable & Cost-Effective**: Runs on standard hardware with open-source tools, no specialized OMR scanners needed  

---

## 🛠️ Prerequisites

- 🐍 Python 3.8+
- 🌐 A modern web browser (e.g., Chrome, Firefox) for the Streamlit interface
- 📄 An answer key in JSON format with the structure:

```json
{
  "answers": {
    "Q1": "A",
    "Q2": "B",
    ...
  }
}
````

---

## ⚙️ Installation

### 1. Clone the Repository 📂

```bash
git clone https://github.com/Jitenrai21/MCQsChecker
cd mcq-paper-grader
```

### 2. Create a Virtual Environment (Optional but Recommended) 🧪

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies 📦

```bash
pip install -r requirements.txt
```

`requirements.txt` should contain:

```text
streamlit==1.38.0
opencv-python==4.10.0.84
numpy==1.26.4
pandas==2.2.2
```

### 4. Prepare the Answer Key 🔑

* Place your `answer_key.json` file in the **project root directory**.
* Ensure it follows the correct format as shown in the **Prerequisites**.

---

## 🚀 Usage

### Run the Application ▶️

```bash
streamlit run main.py
```

This will launch the Streamlit server, accessible at: [http://localhost:8501](http://localhost:8501)

---

### Upload an Answer Sheet 📤

1. Open the web interface in your browser.
2. Use the file uploader to select a scanned answer sheet image (`.jpg`, `.png`, or `.jpeg`).
3. The system will:

   * Process the image
   * Detect filled bubbles
   * Compare with the answer key

---

### View Results 📊

* The processed image is displayed.
* A result summary table shows **question-wise correctness**.
* A **progress bar** visualizes the score.
* Final score (e.g., `25/30`) is shown with a success message.

---

## 📂 Project Structure

```text
mcq-paper-grader/
├── main.py              # Main Streamlit application 🎨
├── utils.py             # Helper functions for image processing and analysis 🛠️
├── answer_key.json      # JSON file with correct answers 🔑
├── requirements.txt     # Project dependencies 📋
└── README.md            # This file 📖
```

---

## 📸 Example Answer Sheet Format

The system expects a **standard answer sheet layout**:

* 🗳️ Two columns, 15 questions each (30 questions total)
* 🔢 Four options per question (A, B, C, D)
* ✍️ Bubbles filled with a dark pen or marker

📌 *For best results, ensure the scanned image is clear, with minimal distortion or shadows.*

---

## ⚠️ Limitations

* 📏 Designed for a fixed layout (2 columns, 15 questions per column)
* 🖼️ Performance may vary with poor image quality (e.g., low resolution, smudges)
* ❓ Currently supports only MCQ formats, not open-ended questions

---

## 🔮 Future Enhancements

* 🛠️ Support for customizable answer sheet layouts
* 🌐 Integration with Learning Management Systems (LMS) for result export
* 🤖 Machine learning models to handle low-quality images or ambiguous marks
* 📬 Real-time feedback for students via a student-facing interface

---

## 🤝 Contributing

We welcome contributions! To get started:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. 💾 Commit your changes

   ```bash
   git commit -m "Add your feature"
   ```
4. 🚀 Push to the branch

   ```bash
   git push origin feature/your-feature
   ```
5. 📬 Open a pull request

✅ Please follow **PEP 8** and include relevant tests.

---

## 🙏 Acknowledgments

Built with:

* Streamlit
* OpenCV
* Pandas

Inspired by the need for accessible, automated grading solutions in education. 🏫

---

## 📧 Contact

For questions or feedback, reach out at:

**[info@jitenrai.com.np](mailto:info@jitenrai.com.np)**

```


