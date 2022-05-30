stundents = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

passedStudents = [i if i > 50 else "Fail" for i in stundents]

print(passedStudents)
