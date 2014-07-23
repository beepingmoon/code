# by beepingmoon, 2014-07-20
# herd sums, POJ 2140
# http://poj.org/problem?id=2140

N = input("Give N from 1 to 10m: ")
start = None
seq = xrange(1,N+1)
# passes would represent position in sequence
passes = 0
# counter will hold a value of possible sums
counter = 0
# algorithm
while passes != N:
	start = seq[passes]
	sum_pattern = 0
	for i in xrange(start,N+1):
		sum_pattern += i
		if sum_pattern == N:
			counter += 1
		elif sum_pattern > N:
			break
	passes += 1
print counter

# ~66 seconds for biggest input (result: 8)
