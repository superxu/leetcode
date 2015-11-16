#!/usr/bin/env python3

'''
Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''

'''
Thoughts: It is a sorted array, then duplicates must be neighbours. For example, [1,1,1,2,2,2,3]
But cannot be [1, 2, 1]
'''

import sys


def main():
	# check number of arguments
    if (len(sys.argv) < 2):
        print("Usage: ./filename 1,1,1,1,2,2...")
        return

    testarray = [int(i) for i in sys.argv[1].split(',')]
    #implementation
    if not testarray:
        return 0
    if len(testarray) == 1:
        return 1

    for i in range(0, len(testarray)):
        if not testarray[i]:
            continue

        for j in range(i+1, len(testarray)):
            if testarray[i] == testarray[j]:
                testarray[j] = None

    # cannot use for...in because remove will change the index
    value = None
    while value in testarray:
        testarray.remove(value)
        

    return len(testarray)
        



if __name__ == "__main__":
	main()