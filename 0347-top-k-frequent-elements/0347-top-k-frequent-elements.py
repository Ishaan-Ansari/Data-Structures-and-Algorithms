from collections import defaultdict
from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans = []

        for num in nums:
            freq[num] += 1

        q = PriorityQueue()
        
        for key, val in freq.items():
            q.put((-val, key))

        for _ in range(k):
            if not q.empty():
                ans.append(q.get()[1])

        return  ans



        