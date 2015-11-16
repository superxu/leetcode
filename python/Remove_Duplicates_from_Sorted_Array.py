#!/usr/bin/env python3

'''
Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''


import sys


def main():
	# check number of arguments
    if (len(sys.argv) < 2):
        print("Usage: ./filename 1,1,1,1,2,2...")
        return

    #implementation
    testlist = [int(i) for i in sys.argv[1].split(',')]
    print("list = %s" % testlist)
    print("length of original list is : %s" % len(testlist))

    '''
    # This is not right because it will include the last number which will generate error: IndexError: list index out of range

    for i in (0, len(testlist)):
    	for j in (i+1, len(testlist)):
    		if testlist[i] == testlist[j]:
    			testlist.pop(j)
    '''

    for i in range(0, len(testlist)):
        print("i = %s" % i) 
        if not testlist[i]:
            continue

        for j in range(i+1, len(testlist)):
            print("j = %s" % j) 
            if testlist[i] == testlist[j]:
                testlist[j] = None

    '''
    # This does not work...
    for value in testlist:
        if value is None:
            testlist.remove(value)
    '''

    testlist = [x for x in testlist if x is not None]

    print("new list = %s" % testlist)
    print("length of new list is : %s" % len(testlist))


if __name__ == "__main__":
	main()