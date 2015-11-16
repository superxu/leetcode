int removeDuplicates(int* nums, int numsSize) {
    
    int i = 0, j = 0;

    if ((nums == NULL) || (numsSize == 0))
    {
        return 0;
    }
    
    if (numsSize == 1)
    {
        return 1;
    }
    

    for (j = 1; j < numsSize; j++)
    {
        if (nums[i] == nums[j])
        {
            continue;
        }
        else
        {
            nums[i+1] = nums[j];
            i += 1;
        }
    }

    return i+1;
    
}