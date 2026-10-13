import pandas as pd

def show_menu():
   
    print("=================================")
    print("     STUDENT MARKS ANALYZER      ")
    print("=================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Show Top Student")
    print("4. Show Lowest Student")
    print("5. Show Subject Averages")
    print("6. Search Student")
    print("7. Show Class Statistics")
    print("8. Exit")
    print("========================")
    try:

        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Please enter your choice in number.")
    return 0

df = pd.read_csv("students.csv")

def calculate_results():
    total = df["Math"] + df["Physics"] + df["English"] + df["Computer"]
    df["Total"] = total
    df["Average"] = df["Total"]/4

    df.loc[df["Average"] >= 50, "Status"] = "Pass"
    df.loc[df["Average"] < 50, "Status"] = "Fail"
    df.loc[df["Average"] < 50, "Grade"]  = "F"
    df.loc[df["Average"] >= 50, "Grade"] = "D"
    df.loc[df["Average"] >= 60, "Grade"] = "C"
    df.loc[df["Average"] >= 70, "Grade"] = "B"
    df.loc[df["Average"] >= 80, "Grade"] = "A"
    df.loc[df["Average"] >= 90, "Grade"] = "A+"
calculate_results()

def add_student():
    
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        math = int(input("Enter student math marks: "))
        if math < 0 or math > 100:
            print("Enter a valid marks.")
            return
    except ValueError:
        print("Please enter a valid marks.")
        return
    
    try:
        phy = int(input("Enter student phy marks: "))
        if phy < 0 or phy > 100:
            print("Enter a valid marks.")
            return
    except ValueError:
        print("Please enter a valid marks.")
        return
    
    try:
        eng = int(input("Enter student eng marks: "))
        if eng < 0 or eng > 100:
            print("Enter a valid marks.")
            return
    except ValueError:
        print("Please enter a valid marks.")
        return
    
    try:
        comp = int(input("Enter your comp marks: "))
        if comp < 0 or comp > 100:
            print("Enter a valid marks.")
            return
    except ValueError:
        print("Please enter a valid marks.")
        return
    student = {
        "Name": name,
        "Math": math,
        "Physics": phy,
        "English": eng,
        "Computer": comp
    }
    df.loc[len(df)] = student
    calculate_results()
    df.to_csv("students.csv", index = False)
    print("Student added successfully.")

def view_student():
    if df.empty:
        print("No students found.")
        return
    print("=================================")
    print("       VIEW STUDENT MARKS        ")
    print("=================================")
    print(df)
    print("=================================")

def search_student():
    print("========== SEARCH STUDENT ==========")
    name = input("Enter a student name: ")
    result = df[df["Name"].str.strip().str.lower() == name.strip().lower()]
    if not result.empty:
        print(result)
    else:
        print("Studnet not found.")

def top_student():
    if df.empty:
        print("No students found.")
        return
    print("========== TOP STUDENT ==========")
    max_marks     = max(df["Average"])
    max_student   = df[df["Average"] == max_marks]["Name"].iloc[0]
    total_marks   = df[df["Average"] == max_marks]["Total"].iloc[0]
    grade_marks   = df[df["Average"] == max_marks]["Grade"].iloc[0]
    print("Name:",    max_student)
    print("Average:", max_marks)
    print("Total:",   total_marks)
    print("Grade:",   grade_marks)


def lowest_student():
    if df.empty:
        print("No students found.")
        return
    print("========== LOWEST STUDENT ==========")
    min_marks     = min(df["Average"])
    min_student   = df[df["Average"] == min_marks]["Name"].iloc[0]
    total_marks   = df[df["Average"] == min_marks]["Total"].iloc[0]
    grade_marks   = df[df["Average"] == min_marks]["Grade"].iloc[0]
    print("Lowest student is:", min_student)
    print("Average:", min_marks)
    print("Total:",   total_marks)
    print("Grade:",   grade_marks)

def subj_average():
    if df.empty:
        print("No students found.")
        return
    print("========== SUBJECT AVERAGE ==========")
    math_average  = df["Math"].mean()
    phy_average   = df["Physics"].mean()
    eng_average   = df["English"].mean()
    comp_average  = df["Computer"].mean()
    print(f"Math Average: {math_average:.2f}")
    print(f"Phy Average: {phy_average:.2f}")
    print(f"Eng Average: {eng_average:.2f}")
    print(f"Comp Average: {comp_average:.2f}")


def class_statistic():

    if df.empty:
        print("No students found.")
        return
    print("========== CLASS STATISTICS ==========")
    rows = df.shape[0]
    class_average = df["Average"].mean()
    max_marks     = max(df["Average"])
    min_marks     = min(df["Average"])
    passed_students = df[df["Status"] == "Pass"].shape[0]
    fail_students = df[df["Status"] == "Fail"].shape[0]
    print("Total students is:", rows)
    print(f"Class Average: {class_average:.2f}")
    print("Highest Average:", max_marks)
    print("Lowest Average:", min_marks)
    print("Passed Students:", passed_students)
    print("Fail Students:", fail_students)

while True:

    choice = show_menu()

    if choice == 1:

        add_student()

    elif choice == 2:

        view_student()

    elif choice == 3:

        top_student()

    elif choice == 4:

        lowest_student()

    elif choice == 5:

        subj_average()

    elif choice == 6:

        search_student()

    elif choice == 7:

        class_statistic()

    elif choice == 8:
        break

    else:

        print("Invalid choice. Please choose 1-8")