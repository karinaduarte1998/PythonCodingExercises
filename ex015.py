# DESAFIO 15 ☻
# Write a program that asks the quantity of kilometers traveled by
# a rented car as well as the quantity of days it was rented for,
# then calculate the price to pay, knowing that the
# car rent costs R$60 per day and R$0.15 per km driven.

# data collection
d = int(input('Hello, how many days in total have you kept the car?'))
km = float(input('And what distance (in km) the car has traveled during that period?'))

# calculations
pd = int(d * 60)
pkm = float(km * 0.15)
pt = pd + pkm

# output
print('Costs based on amount of days rented: R${:.2f}'.format(pd))
print('Costs based on distance traveled: R${:.2f}'.format(pkm))
print('The price for car rental for {} days\ntraveling the distance of {}km\nwill '
      'be of '
      'R${:.2f} in total. '
      .format(d, km, pt))
