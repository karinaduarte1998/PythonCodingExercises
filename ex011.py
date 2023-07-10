# DESAFIO 11 ☻
# Write a program that reads the width and height of a wall in meters,
# calculates its area and the amount of paint needed to paint it,
# knowing that each liter of paint covers an area of 2m².

# data collection
w = float(input('Em metros, what is the width of your wall?'))
h = float(input('In meters, what is the height of your wall?'))

# calculations
a = float(w * h)
p = float(a / 2)

# output
print('Your wall dimension is {:.1f}x{:.1f}'.format(w,h))
print('The area of your wall is {:.1f}m².'.format(a))
print('You will need {:.2f} litres of paint.'.format(p))

