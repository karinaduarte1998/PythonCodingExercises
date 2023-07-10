# DESAFIO 007 ☻
# Develop a program that reads two student grades, calculates and
# displays their average.

# presentation
name = input('\033[0;35;107mHello, what is your name?')
# data collection
c1 = input('Welcome, \033[1;36;107m{}\033[0;35;107m! What cake did you eat first?'.format(name))
g1 = float(input('\033[0;35;107mSeems \033[31;107myummy\033[35;107m! What grade would you give to \033[1;36;107m{'
                 '}\033[0;35;107m?'.format(c1)))
c2 = input('How about the second cake, what flavour was it?')
g2 = float(input('\033[0;31;107mLucky you~\033[0;35;107m what grade you give to \033[1;36;107m{}\033[0;35;107m?'.format(c2)))

# calculations
avg = float(g1 + g2) / 2

# output
print(
    'Well, \033[1;36;107m{}\033[0;35;107m, based on your review, the baker got an average grade of \033[1;33;107m{:.1f}\033[0;35;107m for his last two batches.'.format(
        name, avg))

print('\033[0;35;107mThanks for your help.\033[1;35;107m♥☻')
