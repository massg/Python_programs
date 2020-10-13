from math import ceil

def isPrime(num):
	if num <= 3:
		return num > 1
	elif num % 2 == 0 or num % 3 == 0:
		return False
	
	i = 5
	while i * i <= num:
		if num % i == 0 or num % (i + 2) == 0:
			return False
		i = i + 6
	
	return True

"""
for i in range(100):
	if(isPrime(i)):
		print(i)
"""
