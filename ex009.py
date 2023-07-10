# DESAFIO 009 ☻
# Make a program that reads any Whole Number and show
# in the screen its multiplication table.

# data collection
n = int(input('\033[31mType a number to show its multiplication table'))

# calculations
m = int(n*1)
m2 = int(n*2)
m3 = int(n*3)
m4 = int(n*4)
m5 = int(n*5)
m6 = int(n*6)
m7 = int(n*7)
m8 = int(n*8)
m9 = int(n*9)
m10 = int(n*10)

# output
print('Your number is {}'.format(n))
print('\033[7;31m-*-' * 12)
print(
              '\033[4;31m| {}x 1= {:2} |\n| {}x 2= {:2} |\n| {}x 3= {:2} |\n| {}x 4= {:2} |\n| {}x 5= {:2} |\n| {'
              '}x 6= {:2} |\n| {}x 7= {:2} '
              '|\n| {}x 8= {:2} |\n| {}x 9= {:2} |\n| {}x 10={:2} |'.format(
                  n, m, n, m2, n, m3, n, m4, n, m5, n, m6, n, m7, n, m8, n, m9, n, m10))
print('\033[7;31m-*-' * 12)