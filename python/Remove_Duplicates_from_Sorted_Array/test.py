class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        if len(nums) == 1:
            return 1
            
        i = 0
        n = len(nums)
        for j in range(1, n):
            if nums[i] == nums[j]:
                continue # means j = j + 1
            else:
                nums[i+1] = nums[j]
                i = i+1
        
        return i+1