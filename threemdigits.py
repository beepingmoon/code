# by beepingmoon, 2014-07-22
# three middle digits, http://rosettacode.org/wiki/Middle_three_digits

# test cases
nums = [123, 12345, 1234567, 987654321, 10001, -10001, -123, -100, 100, -12345]
wrong = [1,2,-1,-10,2002,-2002,0]

def threemdigits(num):
	if num < 0:
		n = str(num)[1:]
	else:
		n = str(num)
	if len(n) == 3:
		return n
	elif len(n) > 3 and len(n) % 2 != 0:
			return n[(len(n)-3)/2:-(len(n)-3)/2]
	else:
		return False

print map(threemdigits,nums)
print map(threemdigits,wrong)
