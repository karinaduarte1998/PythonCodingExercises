# DESAFIO 038 ☻
# Write a program that reads two integers and compares them.
# Displaying a message on the screen:
# - The first value is higher
# - The second value is higher
# - There is no greater value, both are equal

val1 = int(input('\033[32mEnter the first number:'))
val2 = int(input('Enter the second number:'))
if val1 > val2:
    print('The \033[1mfirst\033[0;32m value is higher')
elif val2 > val1:
    print('The \033[1msecond\033[0;32m value is higher')
else:
    print('There is no greater value, \033[1mboth are equal')
