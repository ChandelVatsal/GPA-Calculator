from class_grades import classes, calculate_gpa


math126 = classes("Math 126", 5, 4)
math127 = classes("Math 126", 5, 3.1)

classes_taken = [math126, math127]

print(calculate_gpa(classes_taken))

print(math126.get_name())