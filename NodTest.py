import pytest
import nod
def NodTest(a, b, c):
	def test():
		assert nod.nod(a, b) == c
	return test


test1 = NodTest(5, 10, 5)
test2 = NodTest(20, 40, 20)
test3 = NodTest(81, 72, 9)
test4 = NodTest(63, 21, 21)
