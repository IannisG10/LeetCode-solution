class Solution:
  def merge(self,nums1,nums2,n):
    while nums1 and nums1[-1] == 0:
      nums1.pop()
      
    for i in range(n):
      nums1.append(nums2[i])
      
    nums1.sort()
    
nums1 = [-1,-1,0,0,0,0]
nums2 = [-1,0]
n = len(nums2)

Solution().merge(nums1,nums2,n)
print(nums1)
