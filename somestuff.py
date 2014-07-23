# by beepingmoon, 2014-07-23
# some short functions
# some inspired by haskell list functions
# functions are really unnecessary here
# constructs may be used alone, stripped off

import random

def any(lst,func):
	return len(filter(func,lst)) > 0

def all(lst,func):
	return len(filter(func,lst)) == len(lst)

def product(lst):
	return reduce(lambda x, y: x*y, lst)

def removeDuplicates(lst):
	return list(set(lst))

def getASCIICodes(s):
	return map(ord,list(s))

def getCharsFromASCII(l):
	return ''.join(map(chr,l))

# test for removing duplicates and product
a = [random.randint(1,10) for x in xrange(10)]
print a
print product(a)
print removeDuplicates(a)

# some other haskell-like code

# reversing list
print a[::-1]

# head
if len(a) != 0:
	print a[0]

# tail
if len(a) != 0:
	print a[1:]

# last
if len(a) != 0:
	print a[-1]

# take
num = 3
if num <= len(a):
	print a[:num]
else:
	print a

# drop
if num >= len(a):
	print []
else:
	print a[num:]

# get Nth
nth = 2
if nth > len(a):
	print None
else:
	print a[nth-1]

# split At
if nth <= len(a):
	print (a[:nth-1], a[nth-1:])
else:
	print a

# init
if len(a) != 0:
	print a[:-1]
else:
	print None

# add to front
someElem = 999
a = [someElem] + a
print a

# add to back
a.append(someElem)
print a

# insert into middle
a = a[:len(a)/2] + [someElem] + a[len(a)/2:]

# max / min
print max(a)
print min(a)

# odd / even
def even(x): return x % 2 == 0
def odd(x): return x % 2 != 0
print even(4)
print odd(4)
