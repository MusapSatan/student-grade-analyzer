from confing import PASS_NOTE, MIDTERM_WEIGHT, FINAL_WEIGHT, HOMEWORK_WEIGHT

def add_student_grades(students: list[dict])->None:
    for student in students:
        student["Basari_Notu"] = calculate_student_grade(student)

def calculate_student_grade(student: dict)->float:

    return round(
         student["Vize_Notu"] * MIDTERM_WEIGHT
        + student["Final_Notu"] * FINAL_WEIGHT
        + student["Odev_Notu"] * HOMEWORK_WEIGHT,
        2
)
    
def calculate_average(students: list[dict]) -> float:

    if not students:
        raise ValueError("Student list cannot be empty.")

    notes=[student["Basari_Notu"]  for student in students]
    sum_notes=sum(notes)
    note_count=len(notes)
    average_notes=sum_notes/note_count
    return average_notes

def find_highest(students: list[dict]) -> list[dict]:

    if not students:
       raise ValueError("Student list cannot be empty.")
   
    highest_students = [students[0]]

    for student in students[1:]:
        if student["Basari_Notu"] > highest_students[0]["Basari_Notu"]:
            highest_students = [student]

        elif student["Basari_Notu"] == highest_students[0]["Basari_Notu"]:
            highest_students.append(student)

    return highest_students

def find_lowest(students: list[dict]) -> list[dict]:
   
    if not students:
        raise ValueError("Student list cannot be empty.")
   
    lowest_students = [students[0]]

    for student in students[1:]:
        if student["Basari_Notu"] < lowest_students[0]["Basari_Notu"]:
            lowest_students = [student]

        elif student["Basari_Notu"] == lowest_students[0]["Basari_Notu"]:
            lowest_students.append(student)

    return lowest_students

def get_passed_students(students : list[dict]) -> list[dict]:
   return [student for student in students if student["Basari_Notu"] >= PASS_NOTE]
   
def get_failed_students(students : list[dict]) -> list[dict]:
   
   return [student for student in students if student["Basari_Notu"] < PASS_NOTE]

def prepare_histogram_data(students : list[dict]) -> list[float]:
    return [student["Basari_Notu"]  for student in students] 

