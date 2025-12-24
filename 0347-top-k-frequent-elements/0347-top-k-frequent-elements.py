from collections import defaultdict
import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        # frequency of each element
        for num in nums:
            freq[num] += 1

        # push the element in heap
        heap = []
        for num, f in freq.items():
            hq.heappush(heap, (f, num))
            if len(heap)>k:
                hq.heappop(heap)

        res = [num for (_f, num) in heap]
            
        return res
        