# Student Marks Analyzer 📊

A beginner-friendly Python project that analyzes student marks using **Pandas** and CSV files. It calculates totals, averages, grades, and pass/fail status while providing useful class statistics through an interactive command-line menu.

## ✨ Features

- **Add Student:** Add a student's name and marks in four subjects.
- **View Students:** Display student records in a tabular format.
- **Top Student:** Find the student with the highest average.
- **Lowest Student:** Find the student with the lowest average.
- **Subject Averages:** Calculate average marks for each subject.
- **Search Student:** Search for students by name, ignoring capitalization and surrounding spaces.
- **Class Statistics:** Display total students, class average, highest and lowest averages, and pass/fail counts.
- **Automatic Calculations:** Calculate total marks, average, grade, and pass/fail status.
- **Input Validation:** Validate student names and marks.
- **CSV Storage:** Save student records in a CSV file so the data can be reused.

## 🛠️ Technologies Used

- Python
- Pandas
- CSV file handling
- Command-line interface (CLI)

## 📁 Project Structure

```text
student-marks-analyzer/
├── student_analyzer.py
├── students.csv
└── README.md
```

## ⚙️ Requirements

- Python 3.10 or newer
- Pandas

## 🚀 Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/murtaz-ai/student-marks-analyzer.git
```

**2. Open the project directory**

```bash
cd student-marks-analyzer
```

**3. Install Pandas**

```bash
python -m pip install pandas
```

**4. Run the application**

```bash
python student_analyzer.py
```

## 📋 Menu Options

```text
=================================
     STUDENT MARKS ANALYZER
=================================
1. Add Student
2. View Students
3. Show Top Student
4. Show Lowest Student
5. Show Subject Averages
6. Search Student
7. Show Class Statistics
8. Exit
```

## 🧮 Grading System

| Average Marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

**Pass Criteria:** Average marks of 50 or above.

## 💾 Data Storage

Student records are stored in `students.csv`. The application uses Pandas to read and update the data, calculate results, and save new student records.

## 🎯 Learning Objectives

This project helped me practice:

- Python functions and conditional statements
- Loops and input validation
- Exception handling
- Pandas DataFrames and Series
- Filtering rows and selecting columns
- Calculating totals, averages, and statistics
- Reading and writing CSV files
- Building an interactive CLI application

## 🔮 Future Improvements

- Add unique student IDs.
- Edit and delete student records.
- Export class reports.
- Add graphical data visualizations.
- Build a graphical user interface (GUI).

## 👨‍💻 Author

**Murtaz**  
AI Student | Python Developer | Aspiring AI & Machine Learning Engineer

GitHub: [@murtaz-ai](https://github.com/murtaz-ai)

---

*Built as a hands-on Python and data analysis learning project.*