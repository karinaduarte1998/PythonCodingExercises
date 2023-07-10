# DESAFIO 041 ☻
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
actual = date.today().year
dob = int(input('\033[1;36;106mWhat year you were born?'))
age = actual - dob
print('The athlete is {} years old'.format(age))
if age <= 9:
    print('Your swimming category is: little')
elif 9 <= age <= 14:
    print('Your swimming category is: infantile')
elif 14 <= age <= 19:
    print('Your swimming category is: junior')
elif 19 <= age <= 25:
    print('Your swimming category is: senior')
else:
    print('Your swimming category is: master')
