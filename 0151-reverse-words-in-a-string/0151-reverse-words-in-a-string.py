class Solution:
    def _reverse_str(self, temp:str) -> str:
        temp = list(temp)
        i, j = 0, len(temp)-1

        while(i<=j):
            temp[i], temp[j] = temp[j], temp[i]
            i += 1
            j -= 1
        return ''.join(temp)

    def reverseWords(self, s: str) -> str:
        # s = self._reverse_str(s)
        s = s.strip()    # removed preceeding and trailing spaces
        ans = temp = ""
        i = len(s)-1

        while i>=0:
            if s[i] == " ":
                if temp:
                    temp = self._reverse_str(temp)
                    ans += temp + " "
                    temp = ""
                # else:
                #     ans += " "
            
            else:
                temp += s[i]
            i -= 1
        
        if temp:
            ans += self._reverse_str(temp)
        
        return ans.strip()
                