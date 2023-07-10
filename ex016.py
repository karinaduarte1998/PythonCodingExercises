# DESAFIO 16 ☻
# Crie um programa que leia um numero Real pelo teclado e mostre na tela a sua porcao Inteira.
import math
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porcao inteira eh {}'.format(num, math.trunc(num)))
