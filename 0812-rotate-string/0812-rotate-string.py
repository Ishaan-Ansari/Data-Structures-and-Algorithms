class Solution:
    def rotate(self, ans:str):
        ans = list(ans)
        temp = ans[0]

        for i in range(1, len(ans)):
            ans[i-1]=ans[i]
        ans[len(ans)-1] = temp

        return ''.join(ans)

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(0, len(s)):
            s = self.rotate(s)
            if s == goal:
                return True

        return False
                