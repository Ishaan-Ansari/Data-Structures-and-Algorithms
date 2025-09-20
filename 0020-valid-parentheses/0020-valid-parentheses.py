class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        op = {
            "(":1,
            "{":2,
            "[":3,
        }

        cl = {
            ")":1, 
            "}":2, 
            "]":3,
        }

        st = []

        for i in s:
            if i in op:
                st.append(i)

            elif i in cl:
                if not st or op[st[-1]] != cl[i]:
                    return False
                st.pop()

        return len(st)==0
