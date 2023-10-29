# print('Hello, World!')
# program.py
#sum = 1 + 2
#print(sum)
#print("show this in the console")


#sum = 1 + 2 # 3
#product = sum * 2
#print(product)
#planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
#distance_to_alpha_centauri = 4.367 # float, lightyears
#can_liftoff = True
#shuttle_landed_on_the_moon = "Apollo 11" #string

#distance_to_alpha_centauri = 4.367 # looks like a float

#type(distance_to_alpha_centauri) ## <class 'float'>

#<left side> <operator> <right side>#

left_side = 10
right_side = 5
left_side / right_side # 2


'''Operador	Ejemplo
=	x = 2
x ahora contiene 2.
+=	x += 2
x incrementado en 2. Si contenía 2 antes, ahora tiene un valor de 4.
-=	x -= 2
x reducido en 2. Si contenía 2 antes, ahora tiene un valor de 0.
/=	x /= 2
x dividido por 2. Si contenía 2 antes, ahora tiene un valor de 1.
*=	x *= 2
x multiplicado por 2. Si contenía 2 antes, ahora tiene un valor de 4.

from datetime import date
date.today()
print(date.today())
print("Today's date is: " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")'''

