# Challenge 059 ☻ Creating an Options Menu
'''Create a program that reads two values and displays a menu on the screen:
[ 1 ] add
[ 2 ] multiply
[3] bigger
[ 4 ] new numbers
[ 5 ] Exit the program
Your program should perform the requested operation in each case.'''

from time import sleep
for n in range(1, 999):
    n1 = int(input('Type a value'))
    n2 = int(input('Type another value'))
    option = int(input('\n[ 1 ] Add up \n[ 2 ] Multiplication\n[ 3 ] Greater than\n[ 4 ] Type new numbers\n'
                       '[ 5 ] Exit program \nWhat math operation would you like to apply to these values?\n'))
    if option != 5:
        if option == 1:
            soma = n1 + n2
            print(f'The sum between {n1} + {n2} is {soma}.')
        elif option == 2:
            multiplication = n1 * n2
            print(f'The product of the multiplication {n1} x {n2} is {multiplication}.')
        elif option == 3:
            if n1 > n2:
                greater = n1
                print(f'{n1} is greater than {n2}.')
            elif n1 == n2:
                print(f'{n1} and {n2} have equal values.')
            else:
                greater = n2
                print(f'{n2} is greater than {n1}.')
    else:
        break
    sleep(1)
print('Thank you for using our program, goodbye! ☻')
