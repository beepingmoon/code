# by beepingmoon, 2014-06-01
# sum digits

def digit_sum(n):
    result = 0
    while n != 0:
	b = n % 10
	n = n / 10
	result += b
    return result

def sum_digit(num):
    return sum(map(int, list(str(num))))

# test

print digit_sum(1234)
print sum_digit(5436)

# check times
