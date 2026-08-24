import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        lst = defaultdict(list)
        for u, v, w in times:
            lst[u].append((v, w))
        
        time_taken = [float('inf')]*(n+1)
        time_taken[k] = 0
        hq = []
        heapq.heappush(hq, (0, k))

        while hq:
            curr_time, node = heapq.heappop(hq)

            if curr_time > time_taken[node]:
                continue

            for neighbor, nbr_time in lst[node]:
                new_time = curr_time + nbr_time

                if new_time < time_taken[neighbor]:
                    time_taken[neighbor] = new_time
                    heapq.heappush(hq, (new_time, neighbor))

        max_time = max(time_taken[1:])
        
        return max_time if max_time < float('inf') else -1
