name = input('\033[32mWhat is your name?')
print('Nice to meet you\033[36m', name)
age = input('\033[32mHow old are you?')
print('Interesting, {}... you look younger than \033[1m{}'.format(name,age))

