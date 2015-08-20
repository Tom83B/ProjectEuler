import itertools
import pdb

def isabundant(number):
	sumofdivisors = sum( i for i in range(1,number//2+1) if number%i==0 )
	return sumofdivisors>number

ablist = [ i for i in range(1,28123) if isabundant(i) ]
sums = [ x+y for (x,y) in itertools.combinations(ablist, r=2) ]+[ 2*x for x in ablist ]
rest = set(range(1,28123))-set(sums)

print (sum(rest))
