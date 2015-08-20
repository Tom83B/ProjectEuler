import string

f = open('p022_names.txt')
names = f.read()
names = names.replace('"','')
names = names.split(',')
names = sorted(names)

alphabet = string.ascii_uppercase
order = {}
for i in range(0, len(alphabet)):
	order[alphabet[i]] = i+1

namesum = 0

def namescore(name):
	return sum( order[letter] for letter in name )

for i in range(0, len(names)):
	namesum += (i+1)*namescore(names[i])

print (namesum)
