# DESAFIO 034 ☻
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
import math
si = float(input('Qual o valor do salario atualmente?'))
if si > 1250.00:
    sf = si + (si / 100 * 10)
    print('O aumento do salario sera de 10%, sendo o novo salario a quantia de R${:.2f}'.format(sf))
if si <= 1250.00:
    sf = si + (si / 100 * 15)
    print(('O aumento do salario sera de 15%, sendo o novo salario a quantia de R${:.2f}'.format(sf)))

