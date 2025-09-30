class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []

        stack = []

        for i in range(len(asteroids)):
            while stack and asteroids[i]<0 and stack[-1] > 0:
                if stack[-1] == -asteroids[i]:
                    stack.pop()
                    break

                elif stack[-1] > -asteroids[i]:
                    break

                else:
                    stack.pop()
                
            else:
                stack.append(asteroids[i])

        return stack
