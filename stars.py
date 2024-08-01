import random
print('How Many allies (non-peepa):')
allies = int(input())
basedie = (random.randint(1, 6))
ally1 = (random.randint(1, 2))
ally2 = (random.randint(1, 2))
ally3 = (random.randint(1, 2))
ally4 = (random.randint(1, 2))
peepa1temp = (random.randint(1, 3))
peepa2temp = (random.randint(1, 3))
peepa3temp = (random.randint(1, 3))
peepa4temp = (random.randint(1, 3))
if peepa1temp == 1:
	peepa1 = 0
if 2 <= peepa1temp <= 3:
	peepa1 = -1
if peepa2temp == 1:
	peepa2 = 0
if 2 <= peepa2temp <= 3:
	peepa2 = -1
if peepa3temp == 1:
	peepa3 = 0
if 2 <= peepa3temp <= 3:
	peepa3 = -1
if peepa4temp == 1:
	peepa4 = 0
if 2 <= peepa4temp <= 3:
	peepa4 = -1
	
	
peepatotal1 = peepa1
peepatotal2 = peepa1 + peepa2
peepatotal3 = peepa1 + peepa2 + peepa3
peepatotal4 = peepa1 + peepa2 + peepa3 + peepa4
	


if allies == 0:
	print('How Many peepas: (0-4)')
	peepas = int(input())
	if peepas == 0:
		grandpeepa = 0 
	if peepas == 1:
		grandpeepa = peepatotal1
	if peepas == 2:
		grandpeepa = peepatotal2 
	if peepas == 3:
		grandpeepa = peepatotal3
	if peepas == 4:
		grandpeepa = peepatotal4 
		
if allies == 1:
	print('How Many peepas: (0-3)')
	peepas = int(input())
	if peepas == 0:
		grandpeepa = 0 
	if peepas == 1:
		grandpeepa = peepatotal1
	if peepas == 2:
		grandpeepa = peepatotal2 
	if peepas == 3:
		grandpeepa = peepatotal3

if allies == 2:
	print('How Many peepas: (0-2)')
	peepas = int(input())
	if peepas == 0:
		grandpeepa = 0 
	if peepas == 1:
		grandpeepa = peepatotal1
	if peepas == 2:
		grandpeepa = peepatotal2 
		
if allies == 3:
	print('How Many peepas: (0-1)')
	peepas = int(input())
	if peepas == 0:
		grandpeepa = 0 
	if peepas == 1:
		grandpeepa = peepatotal1
		
if allies == 4:
	grandpeepa = 0 

		
print(f'{grandpeepa}')

if allies == 0:
	print(f"Main roll = {basedie}")
	print(f"Total roll = {basedie + grandpeepa}")
	exit()
print('type the team captain')
captain = input()	



	
	###########################################
	
if captain == 'toad':
	newbase = basedie
	tempbase = basedie
	
if captain == 'mario':
	tempbase = (random.randint(1, 6))
	newbase = tempbase
	if tempbase == 3:
		newbase = 0
	if tempbase == 4:
		newbase = 7

if captain == 'luigi':
	tempbase = (random.randint(1, 6))
	newbase = (tempbase + 1)
	if 1 <= tempbase <= 3:
		newbase = 1

if captain == 'peach':
	tempbase = (random.randint(1, 6))
	newbase = tempbase
	if 3 <= tempbase <= 5:
		newbase = 4

if captain == 'daisy':
	tempbase = (random.randint(1, 6))
	newbase = tempbase
	if 1 <= tempbase <= 3:
		if allies == 1:
			newbase = 1
		if allies == 2:
			newbase = 2
		if allies == 3:
			newbase = 3
		if allies == 4:
			newbase = 4

if captain == 'wario':
	tempbase = (random.randint(1, 6))
	newbase = (tempbase)
	if 1 <= tempbase <= 2:
		newbase = 0
		print("other: -1 Coins")
	if 3 <= tempbase <= 3:
		newbase = 7
		
if captain == 'waluigi':
	tempbase = (random.randint(1, 3))
	newbase = 6
	if 1 <= tempbase <= 1:
		newbase = 0
		print("other: -2 Coins")
		
if captain == 'yoshi':
	tempbase = (random.randint(1, 6))
	newbase = tempbase
	if tempbase == 1:
		newbase = 0
	if tempbase == 4:
		newbase = 7
	if tempbase == 6:
		newbase = 5
		
if captain == 'toadette':
	tempbase = (random.randint(1, 2))
	newbase = tempbase
	if tempbase == 1:
		newbase = 3
	if tempbase == 2:
		newbase = 4
		
if captain == 'diddy':
	tempbase = (random.randint(1, 2))
	newbase = tempbase
	if tempbase == 1:
		newbase = 7
	if tempbase == 2:
		newbase = 0
		
if captain == 'donkey':
	tempbase = (random.randint(1, 3))
	newbase = 0
	if tempbase == 1:
		newbase = 10
		
if captain == 'rosalina':
	print("current place (1-4):")
	place = int(input())
	tempbase = (random.randint(1, 6))
	newbase = tempbase
	if 1 <= tempbase <= 4:
		if place == 1:
			newbase = 1
		if place == 2:
			newbase = 2
		if place == 3:
			newbase = 3
		if place == 4:
			newbase = 4
	
	
		
		

	
	
if allies == 1:
	print(f"Main roll = {newbase}")
	print(f"Ally 1 roll = {ally1}")
	print(f"Total roll = {newbase + ally1 + grandpeepa}")
if allies == 2:
	print(f"Main roll = {newbase}")
	print(f"Ally 1 roll = {ally1}")
	print(f"Ally 2 roll = {ally2}")
	print(f"Total roll = {newbase + ally1 + ally2 + grandpeepa}")
if allies == 3:
	print(f"Main roll = {newbase}")
	print(f"Ally 1 roll = {ally1}")
	print(f"Ally 2 roll = {ally2}")
	print(f"Ally 3 roll = {ally3}")
	print(f"Total roll = {newbase + ally1 + ally2 + ally3 + grandpeepa}")
if allies == 4:
	print(f"Main roll = {newbase}")
	print(f"Ally 1 roll = {ally1}")
	print(f"Ally 2 roll = {ally2}")
	print(f"Ally 3 roll = {ally3}")
	print(f"Ally 4 roll = {ally4}")
	print(f"Total roll = {newbase + ally1 + ally2 + ally3 + ally4 + grandpeepa}")
	
exit()
