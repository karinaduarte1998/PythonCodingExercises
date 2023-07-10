# DESAFIO 13 ☻
# Make an algorithm that reads an employee's salary and
# displays his new salary, with a 15% increase.

# data collection
s = float(input('How much is the employee being paid with the current salary?'))

# calculations
si = float(s / 100) * 15
sf = float(si + s)

# output
print('The salary increase will be of {:.2f}, totalizing an amount of {:.2f} as the new salary payment.'.format(si,sf))
