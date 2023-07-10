# DESAFIO 063 ☻
''' Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e
 mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 '''

'''n = int(input('Type a number to see its first Fibonacci sequence numbers: '))
fib1 = n + n
fib2 = fib1 + n
fib3 = fib2 + fib1
fib4 = fib3 + fib2
fib5 = fib4 + fib3
print(f'The first 5 terms using Fibonacci sequence of number {n} is: {fib1} - {fib2} - {fib3} - {fib4} - {fib5} ')
'''
# Resolução

print('-' * 30)
print('Fibonacci Sequence')
print('-' * 30)
n = int(input('How many terms you want to show? '))
t1 = 0  # traditional terms
t2 = 1  # traditional terms
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2  # fibonacci formula
    print(' -> {}'.format(t3), end='')
    t1 = t2  # reevaluate numbers according to sequence (make t1,t2 and t3 the last numbers of sequence and re-calculate)
    t2 = t3
    cont += 1
print('-> FIM')
