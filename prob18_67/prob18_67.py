import sys
import pdb

f = open(sys.argv[1])

rows = []

for line in f:
	rows.append(line.split())
	for i in range(0,len(rows[-1])):
		rows[-1][i] = int(rows[-1][i])

def max_path(rows):
	rows = rows[::-1]
	for i in range(1,len(rows)):
		for j in range(0,len(rows[i])):
			rows[i][j] += max(rows[i-1][j],rows[i-1][j+1])
	return rows[::-1][0][0]

print(max_path(rows))
