# DESAFIO 035 ☻
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
import time
from time import sleep
a = float(input('\033[32;40mQual a medida da primeira reta?'))
b = float(input('Qual a medida da segunda reta?'))
c = float(input('Qual a medida da terceira reta?'))

print('Analisando se as segmentas podem formar um triângulo...')
time.sleep(1.5)
if a < b + c and b < a + c and c < b + a:
    print('\nOs seguimentos PODEM formar um triângulo')
else:
    print('\ns seguimentos NAO podem formar um triângulo!')

