# DESAFIO 026 ☻
# Write a program that reads a phrase from keybord and show:
# How many times letter 'A' appeared
# In what position it appeared first
# In what position it appeared last

fr = str(input('Give me a phrase')).strip().upper()

print('The letter A appeared {} times in the phrase'.format(fr.count('A')))
print('The first letter A appeared in {} position'.format(fr.find('A')+1))
print('The last letter A appeared in {} position'.format(fr.rfind('A')+1))
