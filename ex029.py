# DESAFIO 029 ☻
# Write a program that reads the speed of a car, if it surpasses 80km/h,
# show a message saying he got a fine.
# The fine must cost R$7.00 per each KM over the permitted limit.

speed = float(input('Car Speed in km/h:'))
fine = (speed - 80) * 7
if speed >= 81:
    print('That speed surpasses the limit allowed!')
    print('You must pay a fine of R${:.2f}'.format(fine))
#if speed <= 80:
    print('Drive carefully. Have a good day!')
