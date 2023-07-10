# DESAFIO 017 ☻
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
ca = float(input('Digite o comprimento do cateto adjacente'))
co = float(input('Digite o comprimento do cateto oposto'))
hi = hypot(ca, co)
print('O comprimento da hipotenusa sera de {:.2f}'.format(hi))
