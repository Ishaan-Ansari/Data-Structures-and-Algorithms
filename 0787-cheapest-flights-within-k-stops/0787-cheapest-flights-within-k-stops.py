import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        # create a adjecency list
        for f, t, p in flights:
            adj[f].append((t, p))

        min_stops = [float('inf')]*n

        hq = []
        # current_cost, current_node, stops_taken
        heapq.heappush(hq, (0, src, 0))

        while hq:
            curr_dist, curr_node, stops = heapq.heappop(hq)

            if curr_node == dst:
                return curr_dist

            # k stops means a maximum of k + 1 flights
            if stops == k+1:
                continue

            # If we've already been to this node with FEWER or EQUAL stops
            if stops >= min_stops[curr_node]:
                continue

            min_stops[curr_node] = stops

            for neighbor, price in adj[curr_node]:
                heapq.heappush(hq, (curr_dist+price, neighbor, stops+1))

        return -1       
