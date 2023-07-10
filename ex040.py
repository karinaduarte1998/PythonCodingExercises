# DESAFIO  ☻
# Create a program that reads two grades from a student and calculates their average,
# showing a message at the end, according to the average achieved:
# - Average below 5.0: FAIL
# - Average between 5.0 and 6.9: RECOVERY
# - Average 7.0 or higher: APPROVED

grade1 = float(input('\033[1;37;107mFirst grade: '))
grade2 = float(input('Second grade: '))
score = (grade1 + grade2) / 2
print('The average grade between {:.1f} and {:.1f} is {:.1f}'.format(grade1, grade2, score))
if 7 > score >= 5.0:
    print('The student is in RECOVERY')
elif score < 5.0:
    print('The student has FAILED')
elif score >= 7.0:
    print('The student is APPROVED')
