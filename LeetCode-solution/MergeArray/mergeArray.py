class Solution:
  def mergeArray(self,nums1,nums2,m,n):
    while nums1 and nums1[-1] == 0:
      nums1.pop()

    for i in range(n):
      nums1.append(nums2[i])

    nums1.sort()

array1 = [1,2,3,4,0,0]
array2 = [2,4,5,6]

m = len(array1)
n = len(array2)

Solution().mergeArray(array1,array2,m,n)
print(array1)
      
    
