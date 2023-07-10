n = input('\033[1;32;107mType anything:')
print('\033[1;32;107mIs that a \033[1;31mnumber?\033[1;32m', n.isnumeric())
print('\033[1;32;107mIs that \033[1;31malphabetized?\033[1;32m', n.isalpha())
print('\033[1;32;107mIs that \033[1;31malphanumeric?\033[1;32m', n.isalnum())
print('\033[1;32;107mIs that \033[1;31mcapitalized?\033[1;32m', n.istitle())
print('\033[1;32;107mIs that only \033[1;31mspace?\033[1;32m', n.isspace())
print('\033[1;32;107mIs that \033[1;31mall in capital letters?\033[1;32m', n.isupper())
print('\033[1;32;107mIs that \033[1;31mall in lower case letters?\033[1;32m', n.islower())

