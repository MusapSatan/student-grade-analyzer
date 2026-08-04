from pathlib import Path
import csv



def read_students(csv_path: Path) -> list[dict]:
    with open(csv_path, encoding="utf-8") as file:
        students = list(csv.DictReader(file))

    for student in students:
        student["Ogrenci_ID"] = int(student["Ogrenci_ID"])
        student["Vize_Notu"] = int(student["Vize_Notu"])
        student["Final_Notu"] = int(student["Final_Notu"])
        student["Final_Notu"] = int(student["Final_Notu"])
        student["Odev_Notu"] = int(student["Odev_Notu"])
        student["ODevam_Orani_%"] = int(student["Devam_Orani_%"])

    return students