# DESAFIO 054 ☻
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date

#  import datetime from date library to set current year

atual = date.today().year
#  set current year

contmaior = 0
contmenor = 0
#  set variables to add up figures I will be counting

for c in range(0, 7):  # user input of what year he was born 7x
    dob = int(input('Em que ano você nasceu?'))
    if atual - dob >= 18:  # using if condition to figure what count should be added on based on user input
        contmaior += 1  # if current year - dob is greater or equal to 18, count +1 on full age counting variable
    else:
        contmenor += 1  # if current year - dob is smaller than 18 then user is minor, count +1 on minor age counting
        # variable
print(f'Há um total de {contmaior} pessoas maiores de idade e {contmenor} pessoas menores de idade.')  # print
# output giving out number of full age and minors based on collected input
