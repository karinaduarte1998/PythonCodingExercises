# DESAFIO 10 ☻
# Create a program that reads how much money a person has in their
# wallet and shows how many dollars they can buy.
# Consider US$1.00 = R$3.27

# data collection
r = float(input('How much in \033[1;33mBRL Real\033[0m would you like to convert to \033[1;33mUS Dollars\033[0m?'))

# calculations
d = float(r / 3.27)

# output
print('The amount of dollars you will get after conversion is \033[1;33mUS${:.2f}\033[0m.'.format(d))


