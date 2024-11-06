class Exercise:
  def remove_element(self,arr,val):
    l = len(arr)
    j = 0 #index du 1er élément
    
    for i in range(l):
      if arr[i] != val:
        arr[j] = arr[i]
        j += 1 
      else:
        continue 
      
    return j 
    
array = [1,3,2,2,3,1,2,4,3]
exepect_arr = []
value = 3

element = Exercise().remove_element(array,value)

for i in range(element):
  exepect_arr.append(array[i])

print(f"Number of element: {element}")
print(exepect_arr)
