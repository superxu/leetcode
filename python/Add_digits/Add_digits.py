#!/usr/bin/env python3

import sys

def main():
	total = 0
	number = int(sys.argv[1])
	
	while True:
		while number:
			total += number % 10
			#http://stackoverflow.com/questions/33751373/confused-about-the-different-results-between-using-python-2-7-and-python-3-4
			number //= 10

		if total >= 10:
			number = total
			total = 0
		else:
			break

	print("total = %d" % total)


if __name__ == '__main__':
	main()