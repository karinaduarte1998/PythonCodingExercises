# DESAFIO 030 ☻
# Create a program that reads a number and show on the screen if that number
# is PAIR or an ODD number.

num = int(input('Type any number'))
res = num % 2
if res == 0:
    print('{} is a PAIR number'.format(num))
else:
    print('{} is an ODD number'.format(num))
