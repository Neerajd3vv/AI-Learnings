from classes import student

student1 = student("Jim", "Business", 2.5, False)

student2 = student("Pam", "Art", 3.6, False)

print(student1.name)
print(student2.gpa)

print(student1.great_student())
print(student2.great_student())