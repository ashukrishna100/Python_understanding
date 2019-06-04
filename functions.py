### Q. Join ("Ram" ,"is" ,"in" ,"standard" ,3) using args

def join(*args, sep=' ', end='\n', flush=False):
	text=""
	for arg in args:
		text+=""+str(arg)+sep
	return(text)

#print(join("Ram" ,"is" ,"in" ,"standard" ,3))



## kwargs(keyword arguments)
# keyword means dictionary

def summation(**kwargs):
	s = 0
	for key,value in kwargs.items():
		s += value
	return(s)
#print(summation(a=2,b=4,c=10,d=50))


## scope of function

#print(__name__)  ## attributes of model: __main__ if source code is being executed. if the modeule is being imported then the modeule name will come
"""
if __name__=='__main__':
	print("run successfull")
"""

####   using globals function
#import random

from random import *

s = sorted(globals())
"""
for i in s:
	print(i)
	"""
	
	
###### recursive function: that calls itself


#factorial

def fact(n):
	# n! = n*(n-1)
	if n <= 1:
		return 1
	else:
		return (n * fact(n-1))
#print(fact(4))

#fibonacci (0,1) n = (n-1) + (n-2)
def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)
"""		
for i in range(10):
	print(fib(i))
	
"""



####### scope resolution in python

print(locals())
print("\n\n********************\n\n")
print(globals())		