Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

**Steps of the Algorithm**
**Initialization of the Index**:

You start by defining an index j which is initialized to 1. This index will represent the position of the first unique element in the array.

**Linear Traversal of the Array**:

You iterate through the array starting from the second element (index 1). This means you compare each element to the previous element.

**Difference Test**:

For each element arr[i] (where i is the current index), you check if it is different from the previous element arr[i-1].
If arr[i] is different from arr[i-1], it indicates that you have found a new unique element.

**Updating the Unique Element**:

In this case, you copy arr[i] to the position j and increment j by 1. This means you have recorded this unique element at the end of the list of unique elements.

**Continue the Iteration**:

If arr[i] is identical to arr[i-1], you simply continue the iteration without doing anything.

**Final Result**:
At the end of the loop, all unique elements will be in the first positions of the array up to the index j - 1. The rest of the array may contain elements that you do not want (the duplicates), but this does not affect the validity of the list of unique elements.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)
