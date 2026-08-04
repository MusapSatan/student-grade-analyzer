from pathlib import Path

from analyzer import (
    add_student_grades,
    calculate_average,
    find_highest,
    find_lowest,
    get_passed_students,
    get_failed_students,
    prepare_histogram_data,
)
from file_handler import read_students


def main() -> None:
    csv_path = Path("students.csv")

    students = read_students(csv_path)

    if not students:
        print("Student list is empty.")
        return

    add_student_grades(students)

    average = calculate_average(students)
    highest_students = find_highest(students)
    lowest_students = find_lowest(students)
    passed_students = get_passed_students(students)
    failed_students = get_failed_students(students)
    histogram_data = prepare_histogram_data(students)

    print("=" * 50)
    print("STUDENT GRADE ANALYZER")
    print("=" * 50)

    print(f"\nAverage Grade : {average:.2f}")

    print("\nHighest Grade Student(s)")
    for student in highest_students:
        print(
            f"- {student['Ogrenci_Adi']} "
            f"({student['Basari_Notu']:.2f})"
        )

    print("\nLowest Grade Student(s)")
    for student in lowest_students:
        print(
            f"- {student['Ogrenci_Adi']} "
            f"({student['Basari_Notu']:.2f})"
        )

    print(f"\nPassed Students : {len(passed_students)}")
    print(f"Failed Students : {len(failed_students)}")

    print("\nHistogram Data")
    print(histogram_data)


if __name__ == "__main__":
    main()