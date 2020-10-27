import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

d=0
e=0

while True:
	a=int(input("Escull\n\n	1)	parells\n	2)	senars\n"))
	
	b=int(input("\nEscull un numero\n"))

	c=int(b+random.randint(1,5))

	e=e+1

	if a==1 and c%2==0:
		print("\nhas guanyat")
		d=d+1
	elif a==1 and not c%2==0:
		print("\nhas perdut")
	elif a==2 and not c%2==0:
		print("\nhas guanyat")
		d=d+1
	elif a==2 and c%2==0:
		print("\nhas perdut")

	print("\nHas guanyat",d,"partides de",e,"jugades\n\n")

	input("dale al enter para volver a jugar\n")

	cls()