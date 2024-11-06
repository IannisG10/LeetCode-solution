class Solution: 
    def removeElement(self,nums,val):
        l = len(nums)
        j = 0
        for i in range(l):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            else:
                continue
        
        return j

        
