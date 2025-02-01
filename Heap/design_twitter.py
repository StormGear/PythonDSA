from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0 # keep track of the most recent (more negative)
        self.tweetMap = defaultdict(list) # key([userId]) : value(list([count, tweetId]))
        self.followMap = defaultdict(set) # key([userId]) : value(set(followeeId))        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> list[int]:
        res = [] # ordered starting from more negative count(more recent)
        minHeap = [] # ensures most recent (more negative)

        self.followMap[userId].add(userId) # user is a follower of themselves
        # get a single(rightmost, meaning most recent) tweet from each follower of userId
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # start from end of list showing most recent
                count, tweetId = self.tweetMap[followeeId][index] # return followee tweet
                minHeap.append([count, tweetId, followeeId, index - 1]) # track the previous tweet(index-1)


        heapq.heapify(minHeap) # minHeap contains single most recent tweet from each follower of userId
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0: # if there are more tweets by this followeeId
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
