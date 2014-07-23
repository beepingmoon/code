# by beepingmoon, 2014-07-22
# abc problem, http://rosettacode.org/wiki/ABC_Problem

import time

class Blok:
	def __init__(self, znaki, czyDostepny = True):
		self.znaki = znaki
		self.czyDostepny = czyDostepny

	def sprawdzZnaki(self, znak):
		for z in self.znaki:
			if z == znak:
				return True
		return False

bloki = [Blok('ob'),Blok('xk'),Blok('dq'),Blok('cp'),Blok('na'),
  Blok('gt'),Blok('re'),Blok('tg'),Blok('qd'),Blok('fs'),Blok('jw'),
  Blok('hu'),Blok('vi'),Blok('an'),Blok('ob'),Blok('er'),Blok('fs'),
  Blok('ly'),Blok('pc'),Blok('zm')]

def resetuj():
	for b in bloki:
		b.czyDostepny = True

def funkcjaABC(bloki, slowo, indeks):
	if indeks == len(slowo):
		return True
	for blok in bloki:
		if blok.czyDostepny == False:
			continue
		if blok.sprawdzZnaki(slowo[indeks]) == True:
			blok.czyDostepny = False
			if funkcjaABC(bloki, slowo, indeks+1):
				return True
			blok.czyDostepny = True
	return False

# check long arbitrary string in this file
f = open("slowo.txt",'r')
data = f.read()
f.close()

start = time.time()
print funkcjaABC(bloki, data, 0)
print "Czas szukania: %f sekund " % (time.time() - start)
resetuj()

#print funkcjaABC(bloki, 'a', 0)			# true
#resetuj()
#print funkcjaABC(bloki, 'bark', 0)		# true
#resetuj()
#print funkcjaABC(bloki, 'book', 0)		# false
#resetuj()
#print funkcjaABC(bloki, 'treat', 0)		# true
#resetuj()
#print funkcjaABC(bloki, 'common', 0)	# false
#resetuj()
#print funkcjaABC(bloki, 'squad', 0)		# true
#resetuj()
#print funkcjaABC(bloki, 'confuse', 0)	# true
