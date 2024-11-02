class Solution:
  def twoSum(self,array,target):
    l = len(array)
    for i in range(l):
      for j in range(i+1,l):
        if arr[i]+arr[j] == target:
          print(f"[{i},{j}]")
          return 

arr_input = [2,7,11,15]
target = 9
exec_Solution = Solution()
exec_Solution.twoSum(arr_input,target)
      
    
  
