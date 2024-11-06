class Exercise:
  def remove_duplicate(self,array):
    l = len(array) #lenght of the array 
    j = 1 #index of the second element 
    
    for i in range(1,l):
      if array[i] != array[i-1]:
        array[j] = array[i]
        j += 1 
        
    return j # return the number of the element  
     
ex = Exercise()
arr = [1,1,2,2,3,4,5]
remove_arr = []

elem = ex.remove_duplicate(arr)
print(elem) #display the number of uniqu element

for i in range(elem):
  remove_arr.append(arr[i])
  
print(remove_arr)



