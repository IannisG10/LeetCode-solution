class Solution:
  def romanToInt(self,s):
    #Declare a dictionnary to store the common romans number
    romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    num = 0
    #Browse the romans numbers with loop
    for i in range(len(s) - 1):
      #Si le chiffre romain en cours est inférieur au chiffre romain qui le suit,on soustrait
      if romans[s[i]] < romans[s[i + 1]]:
        num -= romans[s[i]]
      else:
        num += romans[s[i]]
        
    num += romans[s[-1]]
    
    return num
    
romToINT = Solution().romanToInt("XXXIV")
print("Le chiffre est:",romToINT)
