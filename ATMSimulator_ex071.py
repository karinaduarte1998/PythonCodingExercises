# Python Exercise 071:
# Create a program that simulates the operation of an ATM. At the beginning, ask the user what
# will be the amount to be withdrawn (integer number) and the program will inform how many bills of each value will
# be delivered.
# NOTE: consider that the cashier has R$50, R$20, R$10 and R$1 bills.

from time import sleep

print('=' * 30)
print('{:^30}'.format('Welcome to WAIFU bank'))
print('=' * 30)
sleep(1)
value = int(input('How much money would you like to withdraw?'))
total = value
bill = 50
totbills = 0
# infinit loop
while True:
    # condition function to check if value is equal or greater than 50
    if total >= bill:
        # takes 50 out of value
        total -= bill
        # add up on bills counter
        totbills += 1
    # condition function in case value equals to 50
    else:
        if totbills > 0:
            print(f'Total is {totbills} banknotes of ${bill}.')
        # diminishes number to create smaller bill notes
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        totbills = 0
        if total == 0:
            break
sleep(2)
print('='*30)
print('Thank you for using WAIFU bank! Have a good day. ☻')

