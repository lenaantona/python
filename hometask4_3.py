# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.

with open('student.txt', 'r', encoding="utf-8") as f1:
    lines = f1.readlines()

with open('student.txt', 'w', encoding="utf-8") as f2:
    for line in lines:
        if '5' in line:
            f2.write(line.replace(line, line.upper()))
        else:
            f2.write(line)
