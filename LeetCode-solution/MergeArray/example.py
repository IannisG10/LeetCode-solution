class Exercise:
  def mergeArray(self,nums1,nums2):
    m = len(nums1) - 1
    n = len(nums2)

    if nums1[m] == 0:
      for i in range (m,-1,-1):
        if nums1[i] == 0:
          nums1.pop()
        else:
          break

    for j in range(n):
       nums1.append(nums2[j])

    print(nums1)

nums1 = [0]
nums2 = [1]



