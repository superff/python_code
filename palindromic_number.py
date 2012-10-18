def isPandrome(x):
	if x < 0:
		return False
	div = 1
	#div has the same number of digit as x
	while x / div >= 10:
		div *= 10
    
  	while x:
  		l = x / div #first digit
  		r = x % 10  #last digit
  		if l != r:
  			return False
  		x = (x % div) / 10
  		div /= 100
  	return True

def findMaxPNumOf3digit():
	#devide the number into 10 segemnts 999 - 899, 899 - 799,.....
	mutiply_list = [i for i in range(999,0,-100)]
	#l list store the Palindrome number, sorted by its value
	#the element in l is [(a,b),a*b]
	l = []
	#the largest Palindrome number so far
	largest_Palindrome_so_far = 0;
	#index
	i = 1
	#if found Palindrome number ,do not loop any more
	while not l and i < len(mutiply_list):
		#first do multiply between 999-900 and 999-900, then 999-800 and 899 - 800, then ...
		for a in range(mutiply_list[0],mutiply_list[i],-1):
			for b in range(mutiply_list[i-1],mutiply_list[i],-1):
				if a * b < largest_Palindrome_so_far:
					break
				if isPandrome(a*b):
					l.append([(a,b),a*b])
					#the last element of the list is the largest number
					largest_Palindrome_so_far = l[-1][1]
					break
		i += 1
	largest_Palindrome = l[-1]
	return largest_Palindrome 

print findMaxPNumOf3digit()

