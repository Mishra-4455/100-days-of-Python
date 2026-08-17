student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}
for n in student_scores:
    if student_scores[n] < 100 and student_scores[n] > 90:
        student_grades [n] = "Outstanding"
    elif student_scores[n] > 80:
        student_grades [n] = "Exceeds Expectation"
    elif student_scores[n] > 70:
        student_grades [n] = "Acceptable"
    else:
        student_grades [n] = "Fail"
print(student_grades)