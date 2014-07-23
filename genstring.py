# by beepingmoon, 2014-06-01
# generating 1MB string for c file reverse.c

import string
import random

chars = [random.choice(string.ascii_lowercase) for x in xrange(1024*1024)]
f = open("random.txt","w")
x = ""
x = x.join(chars)
f.write(x)
f.close()
