# CHALLENGE 067 ☻  
# Python Exercise 067: Write a program that displays the table of several numbers, one at a time,
# for each value entered by the user. The program will stop when the requested number is negative.

while True:
    n = int(input('What number do you want to see its multiplication table?'))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('End')

