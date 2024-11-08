class Exercise:
  def plusOne(self,digits):
    l = len(digits) - 1 
    for i in range(l,-1,-1):
      digits[i] = digits[i] + 1
      if(digits[i]<=9):
        return digits
      else:
        digits[i] = 0
      
      if digits[0] == 0:
        return [1] + digits
      
      
digits = [1,9,6,7]
digitResult = Exercise().plusOne(digits)
print(digitResult)
