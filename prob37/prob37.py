from math import sqrt

trunctables = []
start_primes = [2,3,5,7]

def isprime(n):
	if n==1: return False
	for d in range(2,int(sqrt(n))+1):
		if n%d==0: return False
	return True

def rtrunct(p):
	pstr = str(p)
	if len(pstr)<3:	return True
	else:
		for i in range(2,len(pstr)):
			if not isprime(int(pstr[:i])):
				return False
		return True

test_list = start_primes
while len(trunctables)<11:
	test_list = [ int(str(a)+str(p)) for a in range(1,10) for p in test_list if isprime(int(str(a)+str(p))) ]
	trunctables += [ p for p in test_list if (isprime(int(str(p)[0])) and rtrunct(p)) ]

print(trunctables)
print(sum(trunctables))
