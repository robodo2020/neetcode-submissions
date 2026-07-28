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
        # get all followers last post
        heap = []
        for follower in self.followers[userId]:
            posts = self.posts[follower]
            if posts:
                idx = len(posts) - 1
                time, tid = posts[idx]
                heapq.heappush(heap, (-time, tid, follower, idx))
        res = []
        while heap:
            time, tid, follower, idx = heapq.heappop(heap)
            res.append(tid)
            idx -= 1

            if idx >= 0:
                next_time, next_tid = self.posts[follower][idx]
                heapq.heappush(heap, (-next_time, next_tid, follower, idx))
            if len(res) == 10:
                break
        return res



        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId] and followerId != followeeId:
            self.followers[followerId].remove(followeeId)