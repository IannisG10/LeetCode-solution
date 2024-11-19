class TreeNode:
  def __init__(self,val):
    self.value = val
    self.left = None
    self.right = None
    
class Solution:
  def sortedArrayToBST(self,nums):
    if not nums:
      return None
    
    mid =  len(nums) // 2
    
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid + 1:])
    
    return root
    
    
  #Fonction optionnal,just to display  
  def displayBST(self,root):
    if root:
      print(root.value,end=" ")
      self.displayBST(root.left)
      self.displayBST(root.right)
    
  
    
array = [-3,0,1,3,4,6]
BST = Solution().sortedArrayToBST(array)
Solution().displayBST(BST)

