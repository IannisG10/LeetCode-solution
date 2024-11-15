class Solution(object):
    def merge(self, nums1, m, nums2, n):
      while nums1 and nums1[-1] == 0:
        nums1.pop()
      for i in range(n):
        nums1.append(nums2[i]) 
      nums1.sort()
