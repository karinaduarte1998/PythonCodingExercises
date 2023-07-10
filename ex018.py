# DESAFIO 018 ☻
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angle = float(input('Digite o angulo que voce deseja'))
seno = sin(radians(angle))
print('O angulo de {} tem o SENO de {:.2f}'.format(angle, seno))
cosseno = cos(radians(angle))
print('O cosseno de {} tem o COSSENO DE {:.2f}'.format(angle, cosseno))
tangente = tan(radians(angle))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angle, tangente))

