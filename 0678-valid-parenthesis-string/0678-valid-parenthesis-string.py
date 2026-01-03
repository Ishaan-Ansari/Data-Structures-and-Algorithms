class Solution:
    def checkValidString(self, s: str) -> bool:
        op = []
        st = []

        n = len(s)

        for i in range(n):
            if s[i] == '(':
                op.append(i)

            elif s[i] == '*':
                st.append(i)
            
            else:
                if op:
                    op.pop()
                elif st:
                    st.pop()
                else:
                    return False

        while op and st:
            if op[-1] < st[-1]:
                op.pop()
                st.pop()
            
            else:
                return False

        return len(op)==0