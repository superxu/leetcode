#!/usr/bin/env python3

'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
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
    if len(testarray) <= 2:
        return len(testarray)

    i = 0
    n = len(testarray)
    counter = 0
 
    
    for j in range(1, n):
        if testarray[i] == testarray[j]:
            counter += 1
            if counter < 2:
                testarray[i+1] = testarray[j]
                i += 1
        else:
            testarray[i+1] = testarray[j]
            i += 1
            counter = 0

    
    print("length = %s" % (i+1))
    print("testarray = %s" % testarray)
    return i+1
                
        

if __name__ == "__main__":
	main()