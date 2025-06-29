class Solution:
    def rotate(self, ans:str):
        ans = list(ans)
        temp = ans[0]

        for i in range(1, len(ans)):
            ans[i-1]=ans[i]
        ans[len(ans)-1] = temp

        return ''.join(ans)

    def rotate2(self, ans:str):
        return ans[1:]+ans[0]

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        rotated = s
        for _ in range(len(s)):
            rotated = self.rotate2(rotated)
            if rotated == goal:
                return True

        return False
