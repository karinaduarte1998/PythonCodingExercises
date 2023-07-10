# DESAFIO 006 ☻
# Create an algorithm that reads a number and displays its
# double, triple and square root.

n = int(input('\033[97mType any number'))
d = n * 2
t = n * 3
sr = n ** (1/2)
print('Your number is \033[4;97m{}\033[0;97m.'.format(n))
print('The double of \033[4;97m{}\033[0;97m is \033[4;97m{}\033[0;97m;'.format(n, d))
print('The triple of \033[4;97m{}\033[0;97m is \033[4;97m{}\033[0;97m;'.format(n, t))
print('The square root of \033[4;97m{}\033[0;97m is \033[4;97m{:.2f}\033[0;97m;'.format(n, sr))

