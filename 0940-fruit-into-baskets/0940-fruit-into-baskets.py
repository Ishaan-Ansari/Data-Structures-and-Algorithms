from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0

        n = len(fruits)
        left = 0
        maxi = 0
        counts = defaultdict(int)

        for right, fruit in enumerate(fruits):
            counts[fruit] += 1

            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1

            maxi = max(maxi, right-left+1)


        return maxi
        