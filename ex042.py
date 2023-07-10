# DESAFIO 041 ☻
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

a = float(input('\033[35;40mWhat is the measurement of the first line?'))
b = float(input('What is the measurement of the second line?'))
c = float(input('What is the measurement of the third line?'))

#- ISOSCELES: two equal sides, one different

if a < b + c and b < c + a and c < a + b:
    print('The lines can form a triangle:')
    if a == b == c:
        print('EQUILATERAL')
    elif a != b and b != c and c != a:
        print('SCALENE')
    else:
        print('ISOSCELES')
else:
    print('The lines cannot form a triangle.')

