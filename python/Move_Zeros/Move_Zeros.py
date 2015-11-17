#!/usr/bin/env python3

import sys

def main():

	testarray = [int(i) for i in sys.argv[1].split(',')]

	if len(testarray) == 1:
		return 

	i = 0
	n = len(testarray)

	for j in range(1, n):
		if testarray[i] != 0:
			i += 1
		else:
			if testarray[j] != 0:
				testarray[i] = testarray[j]
				testarray[j] = 0
				i += 1
		




	print(testarray)


if __name__ == '__main__':
	main()