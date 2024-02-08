student_scores = {
   "Alice": [85, 90, 92],
   "Bob": [78,80, 85],
    "Charlie": [92, 88, 95]
}

student_grades1 = student_scores['Alice']
student_grades2 = student_scores['Bob']
student_grades3 = student_scores['Charlie']

#for grade in student_grades:
       #print(grade)


for student, grades in student_scores.items():
   #for grade in grades:
      print(f'{student}:', *grades)

