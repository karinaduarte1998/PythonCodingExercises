# DESAFIO 008 ☻
# Write a program that read a value em meter and exhibits it
# converted in centimeters and millimetres.

# data collection
v = float(input('\033[1;32;107mType a value in meters'))

# calculations
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm =v * 1000

# output
print('Your value {}m converted to centimeters is {:.0f}cm.'.format(v,cm))
print('Your value {}m converted to millimetres is {:.0f}mm.'.format(v,mm))
print('Your value {}m converted into kilometers is {:.3f}km.'.format(v,km))
print('Your value {}m converted to hectometers is {:.3f}hm.'.format(v,hm))
print('Your value {}m converted to deca-meters is {:.3f}dam.'.format(v,dam))
print('Your value {}m converted to decimeters is {:.0f}dm.'.format(v,dm))