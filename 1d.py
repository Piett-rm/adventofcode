import re
tab =  ['one','two','three','four','five','six','seven','eight','nine']
total = 0
with open("1d.txt", "r") as fichier:
	lignes = fichier.read().split()
	allnumber = []
	for ligne in lignes:
		numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', ligne)
		first = numbers[0]
		last = numbers[-1]
		if first in tab:
			first = int(tab.index(first)) + 1
		if last in tab:
			last = int(tab.index(last)) + 1
		number = f"{first}{last}"
		total+=int(number)

print(total)
#54770