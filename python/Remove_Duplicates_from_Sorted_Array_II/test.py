class Solution(object):
    def removeDuplicates(self, testarray):
        """
        :type nums: List[int]
        :rtype: int
        """
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
    
        return i+1