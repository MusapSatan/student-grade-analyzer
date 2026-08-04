# 📊 Student Grade Analyzer

A clean and modular Python application that analyzes student performance from a CSV file using software engineering best practices.

---

## 🎯 Project Goal

The goal of this project is to practice working with CSV files, file handling, data analysis, and clean Python architecture.

The application reads student information from a CSV file, calculates each student's final success grade using configurable weight values, and generates useful statistics about overall class performance.

---

# 🚀 Features

* ✅ Read student data from a CSV file
* ✅ Calculate weighted success grades
* ✅ Compute class average
* ✅ Find the highest scoring student(s)
* ✅ Find the lowest scoring student(s)
* ✅ List passed students
* ✅ List failed students
* ✅ Generate histogram-ready grade data
* ✅ Modular and maintainable project structure
* ✅ Type hints for improved readability

---

# 📂 Project Structure

```text
student-grade-analyzer/
│
├── analyzer.py          # Grade calculations and analysis functions
├── file_handler.py      # CSV file reading
├── config.py            # Project configuration and grading weights
├── main.py              # Application entry point
├── students.csv         # Sample dataset
└── README.md
```

---

# 📄 CSV Format

Example:

```csv
Ogrenci_ID,Ogrenci_Adi,Bolum,Vize_Notu,Final_Notu,Odev_Notu,Devam_Orani_%
1001,Deniz Sahin,Yapay Zeka Muh.,60,51,58,63
1002,Gamze Sahin,Endustri Muh.,36,95,84,57
```

---

# ⚙️ Grade Calculation

Student success grades are calculated using configurable weight values stored in `config.py`.

Example configuration:

```python
MIDTERM_WEIGHT = 0.30
FINAL_WEIGHT = 0.50
HOMEWORK_WEIGHT = 0.20

PASS_NOTE = 60
```

Formula:

```
Success Grade =
(Midterm × 30%)
+ (Final × 50%)
+ (Homework × 20%)
```

---

# 📈 Program Output

The program calculates:

* Average class grade
* Highest scoring student(s)
* Lowest scoring student(s)
* Number of passed students
* Number of failed students
* Histogram-ready grade list

Example output:

```text
==================================================
STUDENT GRADE ANALYZER
==================================================

Average Grade : 61.17

Highest Grade Student(s)
- Can Kara (90.80)

Lowest Grade Student(s)
- Ayse Kilic (29.00)

Passed Students : 52
Failed Students : 48
```

---

# 🛠 Technologies Used

* Python 3
* csv
* pathlib
* Type Hints

---

# 🧠 Concepts Practiced

* File Handling
* CSV Processing
* Modular Programming
* Functional Decomposition
* List Comprehensions
* Dictionaries
* Lists
* Type Hints
* Software Architecture
* Clean Code
* Single Responsibility Principle (SRP)
* Don't Repeat Yourself (DRY)

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/MusapSatan/student-grade-analyzer.git
```

Go to the project folder:

```bash
cd student-grade-analyzer
```

Run the application:

```bash
python main.py
```

---

# 📌 Future Improvements

* Export analysis results to CSV
* Interactive command-line interface (CLI)
* Data visualization with Matplotlib
* Unit tests using pytest
* Support for multiple grading systems
* Statistical metrics (median, standard deviation, etc.)

---

# 👨‍💻 Author

**Musap SATAN**

Artificial Intelligence & Data Engineering Student

Passionate about Python, Machine Learning, Data Engineering, and Software Development.
