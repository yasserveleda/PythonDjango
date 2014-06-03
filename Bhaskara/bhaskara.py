from math import sqrt, pow

print "\n\n----- Calcular Bhaskara -----\n\n"

a=None
b=None
c=None

while a == None:
    try:
        a = int(raw_input('Digite um numero para o A: '))
    except ValueError:
        print "Digite um numero por favor\n"
while b == None:
    try:
        b = int(raw_input('Digite um numero para o B: '))
    except ValueError:
        print "Digite um numero por favor\n"
while c == None:
    try:
        c = int(raw_input('Digite um numero para o C: '))
    except ValueError:
        print "Digite um numero por favor\n"


def funcao( a, b, c ):
    delta=pow(b,2)-4*a*c
    if delta<0:
        delta = 0
    return sqrt(delta)

def x1(a,b,c):
    x1= (-b + funcao( a, b, c))/2*a
    return x1

def x2(a,b,c):
    x2= (-b - funcao( a, b, c))/2*a
    return x2

def imprimir():
    print "\nSeu x1"    
    print x1(a,b,c)
    print "\nSeu x2"
    print x2(a,b,c)
    print "\n\n"

imprimir()







