# by beepingmoon, 2014-07-21
# crazy search, poj 1200
# http://poj.org/problem?id=1200

import string

# load file into variable text
filename = raw_input("Input only the filename of input text without extension: ")
f = open(filename + ".txt", "r")
text = f.read()
f.close()

# strip punctuation, set letters all to lowercase
# split words (strip whitespaces) and append them to list
# get unique words
exclude = set(string.punctuation)
text = ''.join(ch for ch in text if ch not in exclude)
text = text.lower()
words = text.split()
# or words = [w.strip(",.") for w in text.split()]
exclude = set(string.whitespace)
text = ''.join(ch for ch in text if ch not in exclude)
different = set(words)
#print words

# so far so good, give the length of minimal string to search
N = input("Give the size of substring: ")

# delete words that are smaller in length than N
words = filter(lambda w: len(w) >= N, words)
print words

# different characters in text, not used at all
#unique_chars = set(''.join(words))
#print unique_chars

# check whether given number is a prime number, most basic approach, not efficient
def ifPrime(num):
	if num <= 1:
		return False
	counter = 0
	for i in xrange(2,num+1):
		if num % i == 0:
			counter += 1
		if counter > 1:
			return False
	return True

# algorithm
# set highest to None which will contain biggest prime
# set temp to actual word
# make empty substr list for all substrings of that word
# iterate over the word with "sliding window"
# of iterations length
# append the list with every substring found this way
# remove substring duplicates
# count them and check whether it is a prime
# if it is not a prime continue
# else update highest if number of counts is larger than
# highest value so far
highest = -1
for w in words:
	temp = w
	substr = []
	iterations = (len(w) - N) + 1
	for i in xrange(iterations):
		substr.append(temp[i:i+N])
	without_duplicates = len(list(set(substr)))
	if (ifPrime(without_duplicates) == True):
		if without_duplicates > highest:
			highest = without_duplicates

if highest != -1:
	print "Highest prime in text is %d" % (highest)
else:
	print "No prime numbers in text."
