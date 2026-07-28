class Twitter:
    def __init__(self):
        """
        posts <user: [[tweetId, time]]>
        followers <users: {followers}>
        """
        self.posts = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followers[userId].add(userId)
        self.posts[userId].append([self.time, tweetId])
        self.time += 1

    
    def getNewsFeed(self, userId: int) -> List[int]:
        # get all followers post lists
        heap = []
        for follower in self.followers[userId]:
            for time, tid in self.posts[follower]:
                heapq.heappush(heap, (-time, tid))

        # grab 10 most recent
        res = []
        for _ in range(10):
            if not heap:
                break
            _, tid = heapq.heappop(heap)
            res.append(tid)
        return res

        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId] and followerId != followeeId:
            self.followers[followerId].remove(followeeId)