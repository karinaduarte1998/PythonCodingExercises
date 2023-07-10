# Exercise Python 069: Group Data Analysis
#   Create a program that reads the age and gender of multiple people. For
#   each person registered, the program should ask if the user wants to continue or not. At the end, show:
#   A) How many people are over 18 years old.
#   B) how many men were registered.
#   C) how many women are under 20 years old.


# counters to add up user input based on age, number of males and underage females
males = under20_female = adults = 0

# infinity loop to repeat registering users until user inputs flag to quit program
while True:
    user = input('Register name: ')
    age = int(input('Age: '))
    # variable to hold string type of answer
    gender = ' '

    # loop function to repeat question again in case user typed wrong answers, improves user experience by making it
    # more user-friendly
    while gender not in 'MF':
        # collects gender answer first letter and convert to uppercase to making sure input letter is correct for code
        gender = str(input('Gender(M/F):')).strip().upper()[0]

    # counter for number of adults registered
    if age >= 18:
        adults += 1

        # counter for number of males registered
    if gender == 'M':
        males += 1

    # counter for number of females under 20 years old registered
    elif gender == 'F' and age < 20:
        under20_female += 1

    # variable to hold string type of answer
    ans = ' '

    # loop function to repeat question in case user typed wrong answers
    while ans not in 'YN':
        # collects answer and convert to uppercase making sure input letter is correct for code
        ans = str(input('Want to register another person? (Y/N)')).strip().upper()[0]

    # flag to stop running the program
    if ans == 'N':
        break

# shows the statistics based on data collected
print(f'You have registered {under20_female} female(s) under 20 years old')
print(
    f'In total you have registered {adults} adults. {males} is the number of males and {under20_female} is the number of females under 20 years old registered.')

