class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()            
        s.sort()            
        max_num_of_content_child = 0
        j = 0

        for i in range(len(s)):
            if j<len(g) and g[j] <= s[i]:
                max_num_of_content_child += 1
                j += 1
                
        return max_num_of_content_child