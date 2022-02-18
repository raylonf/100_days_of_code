student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for x in student_scores:
    if student_scores[x] <= 70:
        student_grades[x] = 'Fail'
    elif student_scores[x] <= 80:
        student_grades[x] = 'Acceptable'
    elif student_scores[x] <= 90:
        student_grades[x] = 'Exceeds Expectations'
    elif student_scores[x] <= 100:
        student_grades[x] = 'Outstanding'
            
    

# 🚨 Don't change the code below 👇
print(student_grades)