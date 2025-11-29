from typing import List, Dict, Set, Tuple
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.user_tweets: Dict[int, List[Tuple[int, int]]] = {}
        self.following: Dict[int, Set[int]] = {}

    def _ensure_userId(self, userId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        if userId not in self.following:
            self.following[userId] = {userId} # user follows themself
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """Post a new tweet with monotonically increasing time"""
        self._ensure_userId(userId)
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_tweets:
            return []

        min_heap: List[Tuple[int, int]] = [] 
        for fid in self.following[userId]:
            for ts, tid in self.user_tweets.get(fid, []):
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (ts, tid))
                else:
                    # if this tweet is newer than the smallest of the top-10, replace it
                    if ts > min_heap[0][0]:
                        heapq.heapreplace(min_heap, (ts, tid))
        min_heap.sort(reverse=True)
        return [tid for _, tid in min_heap]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self._ensure_userId(followerId)
        self._ensure_userId(followeeId)
        self.following[followerId].add(followeeId)       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followerId != followeeId:
            self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)