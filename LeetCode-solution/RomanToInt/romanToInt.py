class Solution(object):
    def romanToInt(self, s):
        dict_romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        for i in range(len(s) - 1):
            if dict_romans[s[i]]< dict_romans[s[i + 1]]:
                res -= dict_romans[s[i]]
            else:
                res += dict_romans[s[i]]

        res += dict_romans[s[-1]]
        return res 
        
