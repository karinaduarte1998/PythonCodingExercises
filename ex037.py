# DESAFIO 037 ☻
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

from time import sleep

num = int(input('\033[1;30;107mEnter a integer:'))
base = int(input('Choose one of the basis for conversion:'
                 '\n[1] for binary\n[2] for octal\n[3] for hexadecimal'))
print('Analyzing according to your option [{}]...'.format(base))
sleep(0.8)
if base == 1:
    print('\033[4;31m{}\033[0;30;107m converted to binary is:\033[1;31m {}'.format(num, bin(num)))
elif base == 2:
    print('\033[4;31m{}\033[0;30;107m converted to octal is:\033[1;31m {}'.format(num, oct(num)))
elif base == 3:
    print('\033[4;31m{}\033[0;30;107m converted to hexadecimal is:\033[1;31m {}'.format(num, hex(num)))
else:
    print('Invalid option. Try again.')

