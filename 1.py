import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

c=0
d=0

while True:
	a=int(input("""Escull cara o creu:

	1)	cara
	2)	creu

"""))

	b=random.randint(1,2)

	d=d+1

	print()

	if b==1:
		print("ha sortit cara")
	elif b==2:
		print("ha sortit creu")

	if b==a:
		print("has guanyat")
		c=c+1
	elif not b==a:
		print("has perdut")

	print()

	print("Has guanyat",c,"partides de",d,"jugades\n\n")

	input("dale al enter para volver a jugar\n")

	cls()