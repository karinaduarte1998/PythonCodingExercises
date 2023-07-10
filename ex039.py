# Make a program that reads the year of a young person's birth and informs, according to his age,
# if he is still going to wait to enlist in the military,
# if it is the exact time to enlist or
# if it is past the time of enlistment.
# Your program should also show the time left or overdue.
from datetime import date
atual = date.today().year
name = input('\033[36;40m *You arrive at military facilities*'
             '\n\033[1;32mAttendant:Hi! What is your name?')
birth = int(input('Alright, {}, what year you were born?'.format(name)))
age = atual - birth
if age == 18:
    print('Attendant:You are due to enlist in the military immediately!')
elif age < 18:
    wait = 18 - age
    ano = atual + wait
    print('Attendant:You are not 18 years old and have to wait {} year(s) to enlist in the military.'.format(wait))
    print('Attendant:You will be eligible to enlist in the year {}'.format(ano))
elif age > 18:
    overdue = age - 18
    ano = atual - overdue
    print('Attendant:You are overdue {} year(s) on your military enlistment!'.format(overdue))
    print('Attendant:You should have enlisted in the year of {}'.format(ano))