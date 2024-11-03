class Solution:
  def remove_duplicate(self,array):
    l = len(array)
    j= 1 #index du premier élément unique
    for i in range(1,l):
      if array[i] != array[i-1]:
        array[j]=array[i]
        j+=1 
      else:
        continue
    
    return j
