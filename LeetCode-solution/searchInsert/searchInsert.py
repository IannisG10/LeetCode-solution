class Solution:
    def searchInsert(self,nums,target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            midlle = (left+right)//2

            if nums[midlle] == target:
                return midlle
            elif nums[midlle] < target:
                left = midlle + 1
            else:
                right = midlle - 1

        return left



        
