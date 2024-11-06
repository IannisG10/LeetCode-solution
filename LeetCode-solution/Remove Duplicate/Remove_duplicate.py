class Solution:
    def removeDuplicates(self,nums):
        l = len(nums)
        j = 1
        for i in range(1,l):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return j
