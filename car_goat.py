import random

def exp():
	doors = [0, 0, 0]
	hit = random.randint(0,2)
	doors[hit] = 1

	all_choice = [0, 1, 2]
	choice = random.randint(0,2)
	left_choice = all_choice
	left_choice.remove(choice)

	open_door = random.choice(left_choice)
	left_choice.remove(open_door)
	change = left_choice[0]

	if doors[choice] == 1:
		return 1 
	elif doors[change] == 1:
		return 2
	else:
		return 0

keep = 0
change = 0
total = 100000

for i in range(total):
	result = exp()
	if result == 1:
		keep += 1
	elif result == 2:
		change += 1
print('KEEP:', keep/total)
print('CHANGE:', change/total)

