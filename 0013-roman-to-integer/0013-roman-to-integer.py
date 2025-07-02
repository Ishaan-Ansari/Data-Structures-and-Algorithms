class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        mp = {}
        mp["I"]=1
        mp["V"]=5
        mp["X"]=10
        mp["L"]=50
        mp["C"]=100
        mp["D"]=500
        mp["M"]=1000

        for i in range(len(s)-1, -1, -1):
            if i==len(s)-1:
                ans += mp.get(s[i])   

            elif mp.get(s[i]) < mp.get(s[i+1]):
                ans -= mp.get(s[i])
    
            elif mp.get(s[i]) >= mp.get(s[i+1]):
                ans += mp.get(s[i])
     
        return ans
