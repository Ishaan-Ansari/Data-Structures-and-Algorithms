class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ord_s_to_t = {}
        ord_t_to_s = {}

        for c1, c2 in zip(s, t):
            if c1 in ord_s_to_t:
                if ord_s_to_t[c1] != c2:
                    return False
            else:
                ord_s_to_t[c1] = c2

            if c2 in ord_t_to_s:
                if ord_t_to_s[c2] != c1:
                    return False
            else:
                ord_t_to_s[c2] = c1

        return True

